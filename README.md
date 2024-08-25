# Fake Follower Detection

This project is a Python-based tool designed to identify and flag fake followers on social media profiles. It uses various criteria such as engagement rate and follower/following ratio to evaluate the authenticity of followers.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files Description](#files-description)
- [Contributing](#contributing)
- [License](#license)

## Overview

With the rise of social media, fake followers have become a common issue for influencers, brands, and businesses. This tool helps in identifying those fake followers by analyzing different parameters of a social media profile.

## Features

- **Engagement Rate Analysis**: Evaluates the engagement rate of followers to detect bots or inactive accounts.
- **Follower/Following Ratio**: Analyzes the ratio to identify potential fake followers.
- **Proxy Support**: Includes proxy support to avoid getting blocked by social media platforms during analysis.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/fakeFollower_project.git
    cd fakeFollower_project
    ```

2. **Install required dependencies:**

    Make sure you have Python installed. Then, install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment:**

    If needed, configure your API keys or other environment variables in a `.env` file.

## Usage

To use the tool, run the `main.py` file. You can provide various inputs such as the social media profile to analyze and other parameters.

```bash
python main.py
```

4. **Files Description**

```main.py```: The entry point of the project. Handles the overall flow and user input.

```detectionModule.py```: Contains the core logic for detecting fake followers. It includes functions to calculate engagement rate, follower/following ratio, and other criteria.

```proxies.py```: Manages proxy configurations to prevent IP blocking during large-scale analysis.


## Thanks for visiting!
