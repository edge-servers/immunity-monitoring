from immunity_monitoring.device.apps import DeviceMonitoringConfig


class SampleDeviceMonitoringConfig(DeviceMonitoringConfig):
    name = 'immunity2.sample_device_monitoring'
    label = 'sample_device_monitoring'


del DeviceMonitoringConfig
