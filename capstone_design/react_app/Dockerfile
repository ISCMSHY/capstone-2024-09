FROM node:21.7.3-alpine
RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY ./package*.json ./
RUN npm install
COPY ./ ./
EXPOSE 3000
ENTRYPOINT ["npm", "run", "start"]