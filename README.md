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
1. Ensure HACS is already installed on Home Assistant https://hacs.xyz/docs/use/
2. In Home Assistant, navigate to **HACS**.
3. Select the 3 dots icon in the top right and choose **Custom repositories**
4. Enter `https://github.com/MattFryer/Hass-Custom-Icons` as the repository and select the type of **Dashboard**. Click on **Add**.
5. **Custom Icons Pack** should now be shown just like any other HACS components when searching for it. Click on **Custom Icons Pack**, then in the bottom right click **DOWNLOAD** then in the popup window that opens click **DOWNLOAD** again.
6. Once download and installation is complete, confirm you wish to **RELOAD** the UI

### Optional - Sitewide availability
By default the icons can only be used inside Lovelace dashboards. To use the icons site wide, such as for custom sidebar links, add the following to the `frontend` section of your Home Assistant `configuration.yaml` file:

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
| <img src="/Assets/Icons/alexa.svg" width="48px"> | cust:alexa  |
| <img src="/Assets/Icons/apple-tv.svg" width="48px"> | cust:apple-tv  |
| <img src="/Assets/Icons/apple-tv-plus.svg" width="48px"> | cust:apple-tv-plus  |
| <img src="/Assets/Icons/audiobookshelf.svg" width="48px"> | cust:audiobookshelf  |
| <img src="/Assets/Icons/bazarr.svg" width="48px"> | cust:bazarr  |
| <img src="/Assets/Icons/bitwarden.svg" width="48px">| cust:bitwarden  |
| <img src="/Assets/Icons/bookstack.svg" width="48px">| cust:bookstack  |
| <img src="/Assets/Icons/calibre-web.svg" width="48px"> | cust:calibre-web  |
| <img src="/Assets/Icons/disney-plus.svg" width="48px"> | cust:disney-plus  |
| <img src="/Assets/Icons/esphome.svg" width="48px"> | cust:esphome  |
| <img src="/Assets/Icons/fileflows.svg" width="48px"> | cust:fileflows  |
| <img src="/Assets/Icons/firetv.svg" width="48px"> | cust:firetv  |
| <img src="/Assets/Icons/fitbit.svg" width="48px"> | cust:fitbit  |
| <img src="/Assets/Icons/get-iplayer.svg" width="48px"> | cust:get-iplayer  |
| <img src="/Assets/Icons/gramps-web.svg" width="48px"> | cust:gramps-web  |
| <img src="/Assets/Icons/hass.svg" width="48px"> | cust:hass  |
| <img src="/Assets/Icons/hbo-go.svg" width="48px">| cust:hbo-go  |
| <img src="/Assets/Icons/homepage.svg" width="48px">| cust:homepage  |
| <img src="/Assets/Icons/hp.svg" width="48px">| cust:hp  |
| <img src="/Assets/Icons/influxdb.svg" width="48px"> | cust:influxdb  |
| <img src="/Assets/Icons/it-tools.svg" width="48px"> | cust:it-tools  |
| <img src="/Assets/Icons/jellyseerr.svg" width="48px"> | cust:jellyseerr  |
| <img src="/Assets/Icons/jellystat.svg" width="48px"> | cust:jellystat  |
| <img src="/Assets/Icons/kasa-smart.svg" width="48px"> | cust:kasa-smart  |
| <img src="/Assets/Icons/layzspa.svg" width="48px"> | cust:layzspa |
| <img src="/Assets/Icons/layzspa-bubbles.svg" width="48px"> | cust:layzspa-bubbles |
| <img src="/Assets/Icons/layzspa-heat.svg" width="48px"> | cust:layzspa-heat  |
| <img src="/Assets/Icons/layzspa-pump.svg" width="48px"> | cust:layzspa-pump  |
| <img src="/Assets/Icons/linkding.svg" width="48px"> | cust:linkding  |
| <img src="/Assets/Icons/linktap.svg" width="48px"> | cust:linktap  |
| <img src="/Assets/Icons/logitech.svg" width="48px"> | cust:logitech  |
| <img src="/Assets/Icons/mariadb.svg" width="48px"> | cust:mariadb  |
| <img src="/Assets/Icons/mealie.svg" width="48px"> | cust:mealie  |
| <img src="/Assets/Icons/mqtt-explorer.svg" width="48px"> | cust:mqtt-explorer  |
| <img src="/Assets/Icons/music-assistant.svg" width="48px"> | cust:music-assistant  |
| <img src="/Assets/Icons/node-red.svg" width="48px"> | cust:node-red  |
| <img src="/Assets/Icons/ntfy.svg" width="48px"> | cust:ntfy  |
| <img src="/Assets/Icons/octoprint.svg" width="48px"> | cust:octoprint  |
| <img src="/Assets/Icons/octoprint-alt.svg" width="48px"> | cust:octoprint-alt  |
| <img src="/Assets/Icons/octopus-energy.svg" width="48px"> | cust:octopus-energy  |
| <img src="/Assets/Icons/ollama.svg" width="48px"> | cust:ollama  |
| <img src="/Assets/Icons/omada.svg" width="48px"> | cust:omada  |
| <img src="/Assets/Icons/openai.svg" width="48px"> | cust:openai  |
| <img src="/Assets/Icons/paperless.svg" width="48px"> | cust:paperless  |
| <img src="/Assets/Icons/peanut.svg" width="48px"> | cust:peanut  |
| <img src="/Assets/Icons/piper.svg" width="48px"> | cust:piper  |
| <img src="/Assets/Icons/planka.svg" width="48px"> | cust:planka  |
| <img src="/Assets/Icons/readarr.svg" width="48px"> | cust:readarr  |
| <img src="/Assets/Icons/ring.svg" width="48px"> | cust:ring  |
| <img src="/Assets/Icons/romm.svg" width="48px"> | cust:romm  |
| <img src="/Assets/Icons/sonoff.svg" width="48px"> | cust:sonoff  |
| <img src="/Assets/Icons/sonos.svg" width="48px"> | cust:sonos  |
| <img src="/Assets/Icons/synology.svg" width="48px"> | cust:synology  |
| <img src="/Assets/Icons/synology-dsm.svg" width="48px">  | cust:synology-dsm  |
| <img src="/Assets/Icons/tado.svg" width="48px"> | cust:tado  |
| <img src="/Assets/Icons/tasmota.svg" width="48px"> | cust:tasmota  |
| <img src="/Assets/Icons/tp-link.svg" width="48px"> | cust:tp-link  |
| <img src="/Assets/Icons/tree-christmas.svg" width="48px"> | cust:tree-christmas  |
| <img src="/Assets/Icons/vscode.svg" width="48px"> | cust:vscode  |
| <img src="/Assets/Icons/watchtower.svg" width="48px"> | cust:watchtower  |
| <img src="/Assets/Icons/wemo.svg" width="48px"> | cust:wemo  |
| <img src="/Assets/Icons/zigbee2mqtt.svg" width="48px"> | cust:zigbee2mqtt  |