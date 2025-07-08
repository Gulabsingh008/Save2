FROM python:3.10.4-slim-buster

# Install required system packages in one step to reduce layers
RUN apt update && \
    apt upgrade -y && \
    apt install -y git curl wget bash neofetch ffmpeg software-properties-common python3-pip && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirement file first (layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir wheel && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy rest of the app files
COPY . .

# Set the default command
CMD ["python3", "-m", "Restriction"]
