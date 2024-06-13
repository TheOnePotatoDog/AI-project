# Use the official Node.js image from the Docker Hub
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install the required dependencies
RUN npm install

# Build the application
RUN npm run build

# Expose the port that the app runs on
EXPOSE 3000

# Run the application
CMD ["npm", "start"]