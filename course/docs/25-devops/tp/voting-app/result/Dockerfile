FROM node:18-slim

# add curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# https://docs.docker.com/reference/dockerfile/#healthcheck
HEALTHCHECK --interval=5s --timeout=5s --retries=2 --start-period=5s \
    CMD curl -f http://localhost:80 || exit 1

WORKDIR /usr/local/app

# have nodemon available for local dev use (file watching)
RUN npm install -g nodemon

COPY package*.json ./

RUN npm ci && \
 npm cache clean --force && \
 mv /usr/local/app/node_modules /node_modules

COPY . .

ENV PORT 80
EXPOSE 80

CMD ["node", "server.js"]
