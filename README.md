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

Additional icons for use in the Home Assistant UI. I initially created this component to add icons for self hosted services I use which weren't available in any other HA icon set. Additional icons have been added where the icons that are available were either out of date (i.e. when the branding had changed but the icon set hadn't been updated to reflect it) or where the available icons had issues (such as poor cropping making them look smaller than other icons in the dashboard).

Whilst this component and the icons within are intended for my own use, feel free to use them in your Home Assistant instance also.

## Adding More Icons
If you would like to add more icons, please [raise an issue](https://github.com/MattFryer/Hass-Custom-Icons/issues) in the Github repository and I'll consider adding. Alternatively, add the icons yourself and [raise a pull request](https://github.com/MattFryer/Hass-Custom-Icons/pulls).

If you just want to show your appreciation, you can sponsor the project or send a one off donation using the links below:

[<img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" height="37px" style="margin: 5px"/>](https://buymeacoffee.com/mattfryer)
[<img src="Assets/Readme/github-sponsors-button.svg" height="37px" style="margin: 5px"/>](https://github.com/sponsors/MattFryer)

## Installation
It is advised to install via HACS (Home Assistand Community Store).
1. Ensure HACS is already installed on Home Assistant https://hacs.xyz/docs/installation/prerequisites/
2. In Home Assistant, navigate to **HACS** -> **Frontend**
3. Select the 3 dots icon in the top right and choose **Custom repositories**
4. Enter `https://github.com/MattFryer/Hass-Custom-Icons` as the repository and select the type of **Dashboard**. Click on **Add**.
5. **Custom Icons Pack** should now be shown just like any other HACS components when searching for it. Click on **Custom Icons Pack**, then in the bottom right click **DOWNLOAD** then in the popup window that opens click **DOWNLOAD** again.
6. Once download and installation is complete, confirm you wish to **RELOAD** the UI

### Optional - Sitewide availability
By default the icons can only be used inside Lovelace dashboards. To use the icons site wide, such as for custom sidebar links, add the following to the `Frontend` section of your Home Assistant `configuration.yaml` file:

```yaml
frontend:
  extra_module_url:
    - /hacsfiles/hass-custom-icons/hass-custom-icons.js
```

> [!TIP]
> For the icons to be shown correctly, you may need to refresh your browser a couple of times after installation or updating the component. 

## Icons
Below are all of the currently available icons in this component and their codes to add them to your Home Assistant dashboards. The component supports browsing and searching for icons in the Home Assistant visual editor, just like when using the in-built Home Assistant MDI icons. Alternatively, you can enter the specific icon code (including the `cust:` prefix) when using the YAML code editor instead.

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
| ![get-iplayer](/Assets/Icons/get-iplayer.svg)  | cust:get-iplayer  |
| ![hass](/Assets/Icons/hass.svg)  | cust:hass  |
| ![hbo-go](/Assets/Icons/hbo-go.svg) | cust:hbo-go  |
| ![homepage](/Assets/Icons/homepage.svg) | cust:homepage  |
| ![hp](/Assets/Icons/hp.svg) | cust:hp  |
| ![influxdb](/Assets/Icons/influxdb.svg)  | cust:influxdb  |
| ![it-tools](/Assets/Icons/it-tools.svg)  | cust:it-tools  |
| ![jellyseerr](/Assets/Icons/jellyseerr.svg)  | cust:jellyseerr  |
| ![jellystat](/Assets/Icons/jellystat.svg)  | cust:jellystat  |
| ![kasa-smart](/Assets/Icons/kasa-smart.svg)  | cust:kasa-smart  |
| ![layzspa](/Assets/Icons/layzspa.svg)  | cust:layzspa |
| ![layzspa-bubbles](/Assets/Icons/layzspa-bubbles.svg)  | cust:layzspa-bubbles |
| ![layzspa-heat](/Assets/Icons/layzspa-heat.svg)  | cust:layzspa-heat  |
| ![layzspa-pump](/Assets/Icons/layzspa-pump.svg)  | cust:layzspa-pump  |
| ![linkding](/Assets/Icons/linkding.svg)  | cust:linkding  |
| ![linktap](/Assets/Icons/linktap.svg)  | cust:linktap  |
| ![logitech](/Assets/Icons/logitech.svg)  | cust:logitech  |
| ![mariadb](/Assets/Icons/mariadb.svg)  | cust:mariadb  |
| ![mealie](/Assets/Icons/mealie.svg)  | cust:mealie  |
| ![music-assistant](/Assets/Icons/music-assistant.svg)  | cust:music-assistant  |
| ![node-red](/Assets/Icons/node-red.svg)  | cust:node-red  |
| ![ntfy](/Assets/Icons/ntfy.svg)  | cust:ntfy  |
| ![octoprint](/Assets/Icons/octoprint.svg)  | cust:octoprint  |
| ![octoprint-alt](/Assets/Icons/octoprint-alt.svg)  | cust:octoprint-alt  |
| ![ollama](/Assets/Icons/ollama.svg)  | cust:ollama  |
| ![omada](/Assets/Icons/omada.svg)  | cust:omada  |
| ![openai](/Assets/Icons/openai.svg)  | cust:openai  |
| ![paperless](/Assets/Icons/paperless.svg)  | cust:paperless  |
| ![peanut](/Assets/Icons/peanut.svg)  | cust:peanut  |
| ![piper](/Assets/Icons/piper.svg)  | cust:piper  |
| ![planka](/Assets/Icons/planka.svg)  | cust:planka  |
| ![readarr](/Assets/Icons/readarr.svg)  | cust:readarr  |
| ![ring](/Assets/Icons/ring.svg)  | cust:ring  |
| ![romm](/Assets/Icons/romm.svg)  | cust:romm  |
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
| ![zigbee2mqtt](/Assets/Icons/zigbee2mqtt.svg)  | cust:zigbee2mqtt  |