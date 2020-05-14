import typing
import numbers

import voluptuous as vol
from zigpy.config import (  # noqa: F401
    CONFIG_SCHEMA,
    SCHEMA_DEVICE,
    CONF_DEVICE,
    CONF_DEVICE_PATH,
    CONF_NWK,
    CONF_NWK_CHANNEL,
    CONF_NWK_CHANNELS,
    CONF_NWK_EXTENDED_PAN_ID,
    CONF_NWK_PAN_ID,
    CONF_NWK_KEY,
    CONF_NWK_TC_ADDRESS,
    CONF_NWK_TC_LINK_KEY,
    CONF_NWK_UPDATE_ID,
    cv_boolean,
)

ConfigType = typing.Dict[str, typing.Any]

VolPositiveNumber = vol.All(numbers.Real, vol.Range(min=0))

CONF_DEVICE_BAUDRATE = "baudrate"
CONF_DEVICE_FLOW_CONTROL = "flow_control"

SCHEMA_DEVICE = SCHEMA_DEVICE.extend(
    {
        vol.Optional(CONF_DEVICE_BAUDRATE, default=115_200): int,
        vol.Optional(CONF_DEVICE_FLOW_CONTROL, default=None): vol.In(
            ("hardware", "software", None)
        ),
    }
)


CONF_ZNP_CONFIG = "znp_config"
CONF_TX_POWER = "tx_power"
CONF_SREQ_TIMEOUT = "sync_request_timeout"
CONF_AUTO_RECONNECT_RETRY_DELAY = "auto_reconnect_retry_delay"

CONFIG_SCHEMA = CONFIG_SCHEMA.extend(
    {
        vol.Required(CONF_DEVICE): SCHEMA_DEVICE,
        vol.Optional(CONF_ZNP_CONFIG, default={}): vol.Schema(
            {
                vol.Optional(CONF_TX_POWER, default=None): vol.Any(
                    None, vol.All(int, vol.Range(min=-22, max=19))
                ),
                vol.Optional(CONF_SREQ_TIMEOUT, default=5): VolPositiveNumber,
                vol.Optional(
                    CONF_AUTO_RECONNECT_RETRY_DELAY, default=5
                ): VolPositiveNumber,
            }
        ),
    }
)
