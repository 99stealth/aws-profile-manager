FROM python:latest

COPY . /aws-profile-switcher
WORKDIR /aws-profile-switcher

RUN mkdir /root/.aws/
COPY .github/tests/credentials /root/.aws/

RUN pip install --upgrade pip && \
    pip install -U wheel twine setuptools && \
    pip install -r requirements.txt

RUN make install