from pipeline.storage import PipelineMixin

from storages.backends.s3boto import S3BotoStorage


class PipelineS3BotoStorage(PipelineMixin, S3BotoStorage):
    pass
