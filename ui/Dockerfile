FROM node:12-alpine
RUN mkdir /ui
WORKDIR /ui
COPY package.json /ui/package.json
RUN npm install
RUN npm i -g serve
COPY . /ui
CMD npm run build && PORT=80 serve -s build