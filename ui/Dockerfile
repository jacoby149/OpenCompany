FROM node:14-alpine AS ui-dev
RUN mkdir /ui
WORKDIR /ui
COPY package.json /ui/package.json
RUN npm install
RUN npm i -g serve
COPY . /ui
FROM ui-dev as ui-deploy
ENV REACT_APP_DEFAULT_API=https://api.web10.network                                                                                                     
RUN npm run build
CMD PORT=80 serve -s build