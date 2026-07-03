# Fake Follower Detection

A Python-based tool designed to identify and flag fake followers on social media profiles. It analyzes various criteria such as engagement rate and follower/following ratio to evaluate account authenticity.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files Description](#files-description)
- [Contributing](#contributing)
- [License](#license)

## Overview

With the rise of social media, fake followers have become a common issue for influencers, brands, and businesses. This tool helps identify fake followers by analyzing different parameters and metrics, providing insights into account authenticity and engagement quality.

## Features

- **Follower/Following Ratio Analysis**: Analyzes the ratio to identify potential fake followers
- **Proxy Support**: Includes proxy support to avoid getting blocked by social media platforms during large-scale analysis
- **Engagement Rate Calculation**: Evaluates engagement metrics to determine account legitimacy

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/DarkRaiderCB/fakeFollowers.git
cd fakeFollowers
```

### 2. Install required dependencies

Make sure you have Python installed. Then, install the necessary Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To use the tool, run the `main.py` file. You can provide various inputs such as the social media profile to analyze and other parameters:

```bash
python main.py
```

## Files Description

- **`main.py`**: The entry point of the project. Handles the overall flow and user input.
- **`detectionModule.py`**: Contains the core logic for detecting fake followers. Includes functions to calculate engagement rate, follower/following ratio, and other criteria.
- **`proxies.py`**: Manages proxy configurations to prevent IP blocking during large-scale analysis.



Thanks for visiting!
