from detectionModule import analyzeFollowers
from proxies import generateProxies
import pandas as pd

print("-"*50)
generateProxies()
fake_followers = analyzeFollowers()
if fake_followers:
    print("-"*50)
    print("Fake followers found:")
    print(fake_followers)
    print("-"*50)
    df = pd.DataFrame(fake_followers, columns=[
                      'Fake Followers', 'Followers', 'Following'])
    df.to_csv('fake_followers.csv', index=False)
    print("-"*50)
    print("Fake followers are saved in fake_followers.csv")
    print("-"*50)
else:
    print("-"*50)
    print("No fake followers found")
    print("-"*50)
