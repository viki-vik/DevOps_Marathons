FROM nginx:latest

COPY ./index.html /usr/share/nginx/

EXPOSE 8080

CMD ["nginx","-g","daemon off;"]
