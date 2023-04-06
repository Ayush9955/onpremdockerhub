
FROM node:alpine

WORKDIR /app

COPY . /app

RUN if [ "npm" = "yarn" ]; then yarn; else npm install; fi

EXPOSE 8080

CMD if [ "npm" = "yarn" ]; then yarn start; else npm start; fi
    