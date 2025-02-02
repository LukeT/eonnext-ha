import logging

from homeassistant.core import HomeAssistant, callback

from homeassistant.components.event import (
    EventEntity,
    EventExtraStoredData,
)
from homeassistant.helpers.restore_state import RestoreEntity

from .base import (OctopusEnergyElectricitySensor)
from ..utils.attributes import dict_to_typed_dict
from ..const import CONFIG_TARIFF_COMPARISON_NAME, CONFIG_TARIFF_COMPARISON_PRODUCT_CODE, CONFIG_TARIFF_COMPARISON_TARIFF_CODE, EVENT_ELECTRICITY_PREVIOUS_CONSUMPTION_TARIFF_COMPARISON_RATES

_LOGGER = logging.getLogger(__name__)

class OctopusEnergyElectricityPreviousConsumptionOverrideRates(OctopusEnergyElectricitySensor, EventEntity, RestoreEntity):
  """Sensor for displaying the previous consumption override's rates."""

  def __init__(self, hass: HomeAssistant, meter, point, config):
    """Init sensor."""

    self._hass = hass
    self._config = config
    self._state = None
    self._last_updated = None

    self._attr_event_types = [EVENT_ELECTRICITY_PREVIOUS_CONSUMPTION_TARIFF_COMPARISON_RATES]
    OctopusEnergyElectricitySensor.__init__(self, hass, meter, point, "event")

  @property
  def unique_id(self):
    """The id of the sensor."""
    return f"eon_next_electricity_{self._serial_number}_{self._mpan}{self._export_id_addition}_previous_consumption_rates_{self._config[CONFIG_TARIFF_COMPARISON_NAME]}"
    
  @property
  def name(self):
    """Name of the sensor."""
    return f"{self._config[CONFIG_TARIFF_COMPARISON_NAME]} Previous Consumption Rates {self._export_name_addition}Electricity ({self._serial_number}/{self._mpan})"

  async def async_added_to_hass(self):
    """Call when entity about to be added to hass."""
    # If not None, we got an initial value.
    await super().async_added_to_hass()
    
    self._hass.bus.async_listen(self._attr_event_types[0], self._async_handle_event)

  async def async_get_last_event_data(self):
    data = await super().async_get_last_event_data()
    return EventExtraStoredData.from_dict({
      "last_event_type": data.last_event_type,
      "last_event_attributes": dict_to_typed_dict(data.last_event_attributes),
    })

  @callback
  def _async_handle_event(self, event) -> None:
    if (event.data is not None and 
        "mpan" in event.data and 
        event.data["mpan"] == self._mpan and 
        "serial_number" in event.data and 
        event.data["serial_number"] == self._serial_number and
        "product_code" in event.data and 
        event.data["product_code"] == self._config[CONFIG_TARIFF_COMPARISON_PRODUCT_CODE] and
        "tariff_code" in event.data and 
        event.data["tariff_code"] == self._config[CONFIG_TARIFF_COMPARISON_TARIFF_CODE]):
      self._trigger_event(event.event_type, event.data)
      self.async_write_ha_state()