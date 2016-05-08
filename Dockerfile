FROM jfloff/alpine-python:3.4-onbuild
MAINTAINER Sven Hartmann <svha0004@stud.hs-kl.de>
COPY ./application/ /application/.
CMD python /application/app.py
