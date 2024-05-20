from immunity_monitoring.check.apps import CheckConfig


class SampleCheckConfig(CheckConfig):
    name = 'immunity2.sample_check'
    label = 'sample_check'


del CheckConfig
