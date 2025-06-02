# Home Assistant Additional Icons

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Additional icons for use in Home Assistant UI

## Installation
It is advised to install via HACS (Home Assistand Community Store).
1. Ensure HACS is already installed on Home Assistant https://hacs.xyz/docs/installation/prerequisites/
2. In Home Assistant, navigate to **HACS** -> **Frontend**
3. Select the 3 dots icon in the top right and choose **Custom repositories**
4. Add this repository `https://github.com/MattFryer/Hass-Custom-Icons`
5. **Custom Icons Pack** should be shown as a new repository available to install. Click **INSTALL** then **INSTALL**
6. Confirm you wish to **RELOAD** the UI

### Optional - Sitewide availability
By default the icons can only be used inside Lovelace dashbaords. To use the icons site wide, add the following to the `Frontend` sections of your Home Assistant `configuration.yaml`:

```yaml
frontend:
  extra_module_url:
    - /hacsfiles/hass-custom-icons/hass-custom-icons.js
```

You may need to refresh your browser a couple of times for the icons to be shown the first time.

## Icons
Below are all of the currently available icons in this repository and their codes to add them to your Home Assistant dashboards:

| Icon          | Code          |
| ------------- | ------------- |
| ![alexa](/Assets/Icons/alexa.svg) | cust:alexa  |
| ![apple-tv](/Assets/Icons/apple-tv.svg)  | cust:apple-tv  |
| ![apple-tv](/Assets/Icons/apple-tv-plus.svg)  | cust:apple-tv-plus  |
| ![audiobookshelf](/Assets/Icons/audiobookshelf.svg)  | cust:audiobookshelf  |
| ![bitwarden](/Assets/Icons/bitwarden.svg) | cust:bitwarden  |
| ![bookstack](/Assets/Icons/bookstack.svg) | cust:bookstack  |
| ![calibre-web](/Assets/Icons/calibre-web.svg)  | cust:calibre-web  |
| ![disney-plus](/Assets/Icons/disney-plus.svg)  | cust:disney-plus  |
| ![esphome](/Assets/Icons/esphome.svg)  | cust:esphome  |
| ![firetv](/Assets/Icons/firetv.svg)  | cust:firetv  |
| ![fitbit](/Assets/Icons/fitbit.svg)  | cust:fitbit  |
| ![hass](/Assets/Icons/hass.svg)  | cust:hass  |
| ![hbo-go](/Assets/Icons/hbo-go.svg) | cust:hbo-go  |
| ![hp](/Assets/Icons/hp.svg) | cust:hbo-go  |
| ![influxdb](/Assets/Icons/influxdb.svg)  | cust:hp  |
| ![kasa-smart](/Assets/Icons/kasa-smart.svg)  | cust:kasa-smart  |
| ![layzspa-heat](/Assets/Icons/layzspa-heat.svg)  | cust:layzspa-heat  |
| ![layzspa-pump](/Assets/Icons/layzspa-pump.svg)  | cust:layzspa-pump  |
| ![logitech](/Assets/Icons/logitech.svg)  | cust:logitech  |
| ![mariadb](/Assets/Icons/mariadb.svg)  | cust:mariadb  |
| ![mealie](/Assets/Icons/mealie.svg)  | cust:mealie  |
| ![node-red](/Assets/Icons/node-red.svg)  | cust:node-red  |
| ![ollama](/Assets/Icons/ollama.svg)  | cust:ollama  |
| ![openai](/Assets/Icons/openai.svg)  | cust:openai  |
| ![paperless](/Assets/Icons/paperless.svg)  | cust:paperless  |
| ![piper](/Assets/Icons/piper.svg)  | cust:piper  |
| ![planka](/Assets/Icons/planka.svg)  | cust:planka  |
| ![readarr](/Assets/Icons/readarr.svg)  | cust:readarr  |
| ![ring](/Assets/Icons/ring.svg)  | cust:ring  |
| ![sonoff](/Assets/Icons/sonoff.svg)  | cust:sonoff  |
| ![sonos](/Assets/Icons/sonos.svg)  | cust:sonos  |
| ![synology](/Assets/Icons/synology.svg)  | cust:synology  |
| ![synology-dsm](/Assets/Icons/synology-dsm.svg)   | cust:synology-dsm  |
| ![tado](/Assets/Icons/tado.svg)  | cust:tado  |
| ![tasmota](/Assets/Icons/tasmota.svg)  | cust:tasmota  |
| ![tp-link](/Assets/Icons/tp-link.svg)  | cust:tp-link  |
| ![tree-christmas](/Assets/Icons/tree-christmas.svg)  | cust:tree-christmas  |
| ![wemo](/Assets/Icons/wemo.svg)  | cust:wemo  |

## Adding More Icons
If you would like to add more icons, please [raise an issue](https://github.com/MattFryer/Hass-Custom-Icons/issues) in the Github repository. Alternatively, add the icons yourself and [raise a pull request](https://github.com/MattFryer/Hass-Custom-Icons/pulls).
