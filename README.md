# Line ChatBot

This is a simple LINE chatbot that uses OpenAI to generate responses to user messages.

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages with `pip install -r requirements.txt`.
3. Set your environment variables in a `.env` file in the root directory of the project. This file should include your LINE Channel Secret, LINE Channel Access Token, OpenAI API Key, and OpenAI API Base URL.

## Running the Bot

To run the bot locally, you need to set up a tunneling service like ngrok to expose your local server to the internet. Once you've set up ngrok or a similar service, you can run the bot with `python Line-ChatBot.py`.

Copy the temporary ngrok domain and modify your LineBot Webhook URL accordingly, which should look like this: `https://xxxx.ngrok-free.app/callback`

Verify the webook url, if the status returns success, you will be able to run the Line Chatbot. 

## Deploying to Vercel

You can deploy the bot to Vercel using the Vercel CLI or through GitHub:

### Vercel CLI

1. Install the Vercel CLI with `npm i -g vercel`.
2. Deploy the project with `vercel`.
3. Set your environment variables in the Vercel dashboard.

### GitHub

1. Push your project to a GitHub repository.
2. Log in to Vercel and go to the "Import Project" page.
3. Select "Import Git Repository" and authorize Vercel to access your GitHub account.
4. Select the repository that you want to deploy.
5. Vercel will automatically detect that you're deploying a Python project and fill in the build settings for you. If it doesn't, you can manually set the Build Command to `pip install -r requirements.txt && python Line-ChatBot.py` and the Output Directory to `.`.
6. Click "Deploy" to deploy your project.
7. Set your environment variables in the Vercel dashboard.
