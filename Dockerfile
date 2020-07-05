FROM python:alpine


# ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app
ADD ./cyberhead /app

RUN apk update
RUN apk add -y	pipx

RUN apk add make \
			g++ \
			libssl-dev \
			git \
			vim
RUN pip install pyyaml\
				 termcolor\
				 pandas\
				 .

# RUN npm install -g yarn