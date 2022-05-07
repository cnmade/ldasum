FROM paddlepaddle/paddle:2.2.2

ADD . /ldasum
WORKDIR /ldasum/


RUN python -m pip install paddlehub
RUN python -m pip install flask

RUN python -m pip uninstall opencv-python -y
RUN python -m pip install opencv-python-headless

EXPOSE 5000

CMD ["flask", "run"]