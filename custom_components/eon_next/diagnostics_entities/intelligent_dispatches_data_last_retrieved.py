from .base import OctopusEnergyBaseDataLastRetrieved

class OctopusEnergyIntelligentDispatchesDataLastRetrieved(OctopusEnergyBaseDataLastRetrieved):
  """Sensor for displaying the last time the intelligent dispatches data was last retrieved."""

  def __init__(self, hass, coordinator, account_id):
    """Init sensor."""
    self._account_id = account_id
    OctopusEnergyBaseDataLastRetrieved.__init__(self, hass, coordinator)

  @property
  def unique_id(self):
    """The id of the sensor."""
    return f"eon_next_{self._account_id}_intelligent_dispatches_data_last_retrieved"
    
  @property
  def name(self):
    """Name of the sensor."""
    return f"Intelligent Dispatches Data Last Retrieved ({self._account_id})"