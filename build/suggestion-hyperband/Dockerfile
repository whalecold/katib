FROM cargo.caicloud.xyz/library/python:3.6-slim

RUN if [ "$(uname -m)" = "ppc64le" ] || [ "$(uname -m)" = "aarch64" ]; then \
        apt-get -y update && \
        apt-get -y install gfortran libopenblas-dev liblapack-dev && \
        pip install cython; \
    fi

ADD . /usr/src/app/github.com/kubeflow/katib
WORKDIR /usr/src/app/github.com/kubeflow/katib/cmd/suggestion/hyperband/v1alpha3
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /usr/src/app/github.com/kubeflow/katib:/usr/src/app/github.com/kubeflow/katib/pkg/apis/manager/v1alpha3/python:/usr/src/app/github.com/kubeflow/katib/pkg/apis/manager/health/python

ENTRYPOINT ["python", "main.py"]
