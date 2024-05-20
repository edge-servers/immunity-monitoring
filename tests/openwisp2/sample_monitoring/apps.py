from immunity_monitoring.monitoring.apps import MonitoringConfig


class SampleMonitoringConfig(MonitoringConfig):
    name = 'immunity2.sample_monitoring'
    label = 'sample_monitoring'


del MonitoringConfig
