from .base import OctopusEnergyBaseDataLastRetrieved

class OctopusEnergyIntelligentSettingsDataLastRetrieved(OctopusEnergyBaseDataLastRetrieved):
  """Sensor for displaying the last time the intelligent settings data was last retrieved."""

  def __init__(self, hass, coordinator, account_id):
    """Init sensor."""
    self._account_id = account_id
    OctopusEnergyBaseDataLastRetrieved.__init__(self, hass, coordinator)

  @property
  def unique_id(self):
    """The id of the sensor."""
    return f"eon_next_{self._account_id}_intelligent_settings_data_last_retrieved"
    
  @property
  def name(self):
    """Name of the sensor."""
    return f"Intelligent Settings Data Last Retrieved ({self._account_id})"