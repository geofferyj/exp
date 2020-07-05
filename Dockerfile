FROM python:alpine


# ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app
ADD ./cyberhead /app

RUN apk update

RUN apk add make \
			g++ \
			libressl-dev \
			git \
			vim
RUN pip install pyyaml\
				 termcolor\
				 pandas
				 
RUN python3 -m pip install --user pipx && python3 -m pipx ensurepath

# RUN npm install -g yarn