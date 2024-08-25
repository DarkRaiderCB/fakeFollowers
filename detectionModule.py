import re
from bs4 import BeautifulSoup
import random
import requests
import instaloader
import getpass


def getHeaders():
    headers = {
        "User-agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
        ])
    }
    return headers


def getInstagramData(followerUsername):
    url = f"https://www.instagram.com/{followerUsername}/"
    try:
        with open('proxies.txt', 'r') as file:
            proxies = file.readlines()

        proxies = [proxy.strip() for proxy in proxies]
        if not proxies:
            raise ValueError("No proxies available")

        proxy = random.choice(proxies)
        proxyDict = {'http': proxy}

        response = requests.get(url, headers=getHeaders(),
                                proxies=proxyDict, timeout=10)
        response.raise_for_status()
    except (requests.RequestException, ValueError) as e:
        print(f"Failed to fetch data for {followerUsername}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        profileName = soup.find('meta', property='og:title')['content']
        profileName = re.sub(
            r' • Instagram photos and videos', '', profileName)

        profileDescription = soup.find(
            'meta', property='og:description')['content']
        profileDescription = re.sub(r'[^\w\s]', '', profileDescription)
        profileDescription = profileDescription.split(' ')

        followers = [profileDescription[i - 1]
                     for i in range(len(profileDescription)) if profileDescription[i].lower() == 'followers']
        following = [profileDescription[i - 1]
                     for i in range(len(profileDescription)) if profileDescription[i].lower() == 'following']

        followers = int(followers[0].replace(',', ''))
        following = int(following[0].replace(',', ''))
    except (IndexError, TypeError, ValueError) as e:
        if "M" or "K" in followers or following:
            followers = int(float(followers.replace('M', '')) * 1000000) if 'M' in followers else int(
                float(followers.replace('K', '')) * 1000)
            following = int(float(following.replace('M', '')) * 1000000) if 'M' in following else int(
                float(following.replace('K', '')) * 1000)
        else:
            print(f"Error parsing data for {followerUsername}: {e}")
            return {
                'Profile Name': profileName if 'profileName' in locals() else followerUsername,
                'followers/following ratio': None
            }

    try:
        followerFollowingRatio = followers / following if following > 0 else None
    except ZeroDivisionError:
        followerFollowingRatio = None

    return {
        'Profile Name': profileName,
        'Followers': followers,
        'Following': following,
        'followers/following ratio': followerFollowingRatio,
    }


def flagFake(data):
    fake = []
    for follower in data:
        if follower['Followers'] == 0 and follower['Following'] != 0:
            print(follower)
            print("---------Most likely a private account---------")

        elif follower and follower['followers/following ratio'] is not None and follower['followers/following ratio'] <= 0.05:
            fake.append([follower['Profile Name'],
                        follower['Followers'], follower['Following']])
    return fake


def getFollowers(creatorUsername, L):
    try:
        profile = instaloader.Profile.from_username(L.context, creatorUsername)
        print("Fetching followers... This may take a while.")
        print("-" * 50)
        return [follower.username for follower in profile.get_followers()]
    except instaloader.exceptions.ProfileNotExistsException:
        print("Error: The profile does not exist.")
        return None
    except instaloader.exceptions.QueryReturnedNotFoundException:
        print("Error: Profile not found (404). This could mean the profile does not exist or is private.")
        return None


def analyzeFollowers():
    L = instaloader.Instaloader()

    print("-"*50)
    print("Please enter your Instagram credentials.")

    USERNAME = input("Enter your Instagram username: ")
    PASSWORD = getpass.getpass("Enter your Instagram password: ")
    print("-"*50)

    try:
        print("Logging in...")
        print("-"*50)
        L.login(USERNAME, PASSWORD)
        print("Logged in successfully")
        print("-"*50)
    except instaloader.exceptions.ConnectionException as e:
        print("Failed to connect:", e)
        return []
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("Two-factor authentication required.")
        return []
    except instaloader.exceptions.BadCredentialsException:
        print("Invalid login credentials.")
        return []

    creatorUsername = input(
        "Enter the username of the creator you want to analyze: ")
    print("-"*50)

    followers = getFollowers(creatorUsername, L)
    followersData = []
    for follower in followers:
        data = getInstagramData(follower)
        if data:
            followersData.append(data)

    fake = flagFake(followersData)
    return fake
