# Home Assistant Additional Icons

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub license](https://img.shields.io/github/license/MattFryer/Hass-Custom-Icons.svg?logo=gnu&logoColor=ffffff)](https://github.com/MattFryer/Hass-Custom-Icons/blob/master/LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/MattFryer/Hass-Custom-Icons)
![GitHub last commit](https://img.shields.io/github/last-commit/MattFryer/Hass-Custom-Icons)
![GitHub contributors](https://img.shields.io/github/contributors/MattFryer/Hass-Custom-Icons)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/MattFryer/Hass-Custom-Icons)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/MattFryer/Hass-Custom-Icons)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/MattFryer/Hass-Custom-Icons.svg)](http://isitmaintained.com/project/MattFryer/Hass-Custom-Icons "Average time to resolve an issue")
![GitHub Repo stars](https://img.shields.io/github/stars/MattFryer/Hass-Custom-Icons)
![GitHub forks](https://img.shields.io/github/forks/MattFryer/Hass-Custom-Icons)
![GitHub watchers](https://img.shields.io/github/watchers/MattFryer/Hass-Custom-Icons)

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

> [!TIP]
> You may need to refresh your browser a couple of times for the icons to be shown the first time.

## Icons
Below are all of the currently available icons in this repository and their codes to add them to your Home Assistant dashboards:

| Icon          | Code          |
| ------------- | ------------- |
| ![alexa](/Assets/Icons/alexa.svg) | cust:alexa  |
| ![apple-tv](/Assets/Icons/apple-tv.svg)  | cust:apple-tv  |
| ![apple-tv](/Assets/Icons/apple-tv-plus.svg)  | cust:apple-tv-plus  |
| ![audiobookshelf](/Assets/Icons/audiobookshelf.svg)  | cust:audiobookshelf  |
| ![bazarr](/Assets/Icons/bazarr.svg)  | cust:bazarr  |
| ![bitwarden](/Assets/Icons/bitwarden.svg) | cust:bitwarden  |
| ![bookstack](/Assets/Icons/bookstack.svg) | cust:bookstack  |
| ![calibre-web](/Assets/Icons/calibre-web.svg)  | cust:calibre-web  |
| ![disney-plus](/Assets/Icons/disney-plus.svg)  | cust:disney-plus  |
| ![esphome](/Assets/Icons/esphome.svg)  | cust:esphome  |
| ![fileflows](/Assets/Icons/fileflows.svg)  | cust:fileflows  |
| ![firetv](/Assets/Icons/firetv.svg)  | cust:firetv  |
| ![fitbit](/Assets/Icons/fitbit.svg)  | cust:fitbit  |
| ![hass](/Assets/Icons/hass.svg)  | cust:hass  |
| ![hbo-go](/Assets/Icons/hbo-go.svg) | cust:hbo-go  |
| ![hp](/Assets/Icons/hp.svg) | cust:hp  |
| ![influxdb](/Assets/Icons/influxdb.svg)  | cust:hp  |
| ![jellyseerr](/Assets/Icons/jellyseerr.svg)  | cust:jellyseerr  |
| ![kasa-smart](/Assets/Icons/kasa-smart.svg)  | cust:kasa-smart  |
| ![layzspa](/Assets/Icons/layzspa.svg)  | cust:layzspa |
| ![layzspa-bubbles](/Assets/Icons/layzspa-bubbles.svg)  | cust:layzspa-bubbles |
| ![layzspa-heat](/Assets/Icons/layzspa-heat.svg)  | cust:layzspa-heat  |
| ![layzspa-pump](/Assets/Icons/layzspa-pump.svg)  | cust:layzspa-pump  |
| ![logitech](/Assets/Icons/logitech.svg)  | cust:logitech  |
| ![mariadb](/Assets/Icons/mariadb.svg)  | cust:mariadb  |
| ![mealie](/Assets/Icons/mealie.svg)  | cust:mealie  |
| ![node-red](/Assets/Icons/node-red.svg)  | cust:node-red  |
| ![ntfy](/Assets/Icons/ntfy.svg)  | cust:ntfy  |
| ![octoprint](/Assets/Icons/octoprint.svg)  | cust:octoprint  |
| ![octoprint-alt](/Assets/Icons/octoprint-alt.svg)  | cust:octoprint-alt  |
| ![ollama](/Assets/Icons/ollama.svg)  | cust:ollama  |
| ![openai](/Assets/Icons/openai.svg)  | cust:openai  |
| ![paperless](/Assets/Icons/paperless.svg)  | cust:paperless  |
| ![peanut](/Assets/Icons/peanut.svg)  | cust:peanut  |
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
| ![vscode](/Assets/Icons/vscode.svg)  | cust:vscode  |
| ![watchtower](/Assets/Icons/watchtower.svg)  | cust:watchtower  |
| ![wemo](/Assets/Icons/wemo.svg)  | cust:wemo  |

## Adding More Icons
If you would like to add more icons, please [raise an issue](https://github.com/MattFryer/Hass-Custom-Icons/issues) in the Github repository. Alternatively, add the icons yourself and [raise a pull request](https://github.com/MattFryer/Hass-Custom-Icons/pulls).

If you just want to show your appreciation, you can sponsor the project or send a one off donation using the links below:

[<img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" height="37px" style="margin: 5px"/>](https://buymeacoffee.com/mattfryer)
[<img src="Assets/Readme/github-sponsors-button.svg" height="37px" style="margin: 5px"/>](https://github.com/sponsors/MattFryer)