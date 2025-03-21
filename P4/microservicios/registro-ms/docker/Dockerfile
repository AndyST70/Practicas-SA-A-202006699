FROM node:18

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .
COPY wait-for-it.sh .
RUN chmod +x wait-for-it.sh

CMD ["./wait-for-it.sh", "mysql:3306", "--timeout=30", "--", "node", "server.js"]

EXPOSE 4001

