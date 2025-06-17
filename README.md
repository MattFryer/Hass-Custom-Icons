# Home Assistant Additional Icons

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Plugin-Blue?logo=homeassistant&logoColor=%23fff&color=%2303a9f4)](https://www.home-assistant.io/)
[![HACS](https://img.shields.io/badge/HACS-Custom-Blue?logo=homeassistantcommunitystore&logoColor=%23fff&color=%2303a9f4)](https://github.com/custom-components/hacs)
[![GitHub Release](https://img.shields.io/github/v/release/MattFryer/Hass-Custom-Icons)](https://github.com/MattFryer/Hass-Custom-Icons/releases/latest)
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
It is advised to install this Home Assistant plug-in via HACS (the Home Assistant Community Store). If you have HACS installed already you can click this button to quickly add this repository to HACS and open the page ready to install.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=MattFryer&repository=Hass-Custom-Icons&category=Dashboard) 

Alternatively, you can follow the below steps to add this repository to HACS manually as a custom repository and install the plug-in:
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
| <img src="/Assets/Icons/aldi.svg" width="48px" alt="cust:aldi"> | cust:aldi  |
| <img src="/Assets/Icons/alexa.svg" width="48px" alt="cust:alexa"> | cust:alexa  |
| <img src="/Assets/Icons/alexa-plus.svg" width="48px" alt="cust:alexa-plus"> | cust:alexa-plus  |
| <img src="/Assets/Icons/apple-tv.svg" width="48px" alt="cust:apple-tv"> | cust:apple-tv  |
| <img src="/Assets/Icons/apple-tv-plus.svg" width="48px" alt="cust:apple-tv-plus"> | cust:apple-tv-plus  |
| <img src="/Assets/Icons/audiobookshelf.svg" width="48px" alt="cust:audiobookshelf"> | cust:audiobookshelf  |
| <img src="/Assets/Icons/b&q.svg" width="48px" alt="cust:b&q"> | cust:b&q  |
| <img src="/Assets/Icons/bazarr.svg" width="48px" alt="cust:bazarr"> | cust:bazarr  |
| <img src="/Assets/Icons/bbc-micro.svg" width="48px" alt="cust:bbc-micro"> | cust:bbc-micro  |
| <img src="/Assets/Icons/bbc-sounds.svg" width="48px" alt="cust:bbc-sounds"> | cust:bbc-sounds  |
| <img src="/Assets/Icons/bbc-sounds-alt.svg" width="48px" alt="cust:bbc-sounds-alt"> | cust:bbc-sounds-alt  |
| <img src="/Assets/Icons/bitwarden.svg" width="48px" alt="cust:bitwarden">| cust:bitwarden  |
| <img src="/Assets/Icons/bookstack.svg" width="48px" alt="cust:bookstack">| cust:bookstack  |
| <img src="/Assets/Icons/calibre-web.svg" width="48px" alt="cust:calibre-web"> | cust:calibre-web  |
| <img src="/Assets/Icons/disney-plus.svg" width="48px" alt="cust:disney-plus"> | cust:disney-plus  |
| <img src="/Assets/Icons/draw-io.svg" width="48px" alt="cust:draw-io"> | cust:draw-io  |
| <img src="/Assets/Icons/esphome.svg" width="48px" alt="cust:esphome"> | cust:esphome  |
| <img src="/Assets/Icons/evri.svg" width="48px" alt="cust:evri"> | cust:evri  |
| <img src="/Assets/Icons/extractor-hood.svg" width="48px" alt=" cust:extractor-hood"> | cust:extractor-hood  |
| <img src="/Assets/Icons/fileflows.svg" width="48px" alt="cust:fileflows"> | cust:fileflows  |
| <img src="/Assets/Icons/firetv.svg" width="48px" alt="cust:firetv"> | cust:firetv  |
| <img src="/Assets/Icons/fitbit.svg" width="48px" alt="cust:fitbit"> | cust:fitbit  |
| <img src="/Assets/Icons/get-iplayer.svg" width="48px" alt="cust:get-iplayer"> | cust:get-iplayer  |
| <img src="/Assets/Icons/gramps-web.svg" width="48px" alt="cust:gramps-web"> | cust:gramps-web  |
| <img src="/Assets/Icons/hass.svg" width="48px" alt="cust:hass"> | cust:hass  |
| <img src="/Assets/Icons/hbo-go.svg" width="48px" alt="cust:hbo-go">| cust:hbo-go  |
| <img src="/Assets/Icons/homepage.svg" width="48px" alt="cust:homepage">| cust:homepage  |
| <img src="/Assets/Icons/honeywell.svg" width="48px" alt="cust:honeywell">| cust:honeywell  |
| <img src="/Assets/Icons/honeywell-alt.svg" width="48px" alt="cust:honeywell-alt">| cust:honeywell-alt  |
| <img src="/Assets/Icons/hp.svg" width="48px" alt="cust:hp ">| cust:hp  |
| <img src="/Assets/Icons/influxdb.svg" width="48px" alt="cust:influxdb"> | cust:influxdb  |
| <img src="/Assets/Icons/iplayer.svg" width="48px" alt="cust:iplayer"> | cust:iplayer  |
| <img src="/Assets/Icons/iplayer-alt.svg" width="48px" alt="cust:iplayer-alt"> | cust:iplayer-alt  |
| <img src="/Assets/Icons/it-tools.svg" width="48px" alt="cust:it-tools"> | cust:it-tools  |
| <img src="/Assets/Icons/jellyseerr.svg" width="48px" alt="cust:jellyseerr"> | cust:jellyseerr  |
| <img src="/Assets/Icons/jellystat.svg" width="48px" alt="cust:jellystat"> | cust:jellystat  |
| <img src="/Assets/Icons/kasa-smart.svg" width="48px" alt="cust:kasa-smart"> | cust:kasa-smart  |
| <img src="/Assets/Icons/layzspa.svg" width="48px" alt="cust:layzspa"> | cust:layzspa |
| <img src="/Assets/Icons/layzspa-bubbles.svg" width="48px" alt="cust:layzspa-bubbles"> | cust:layzspa-bubbles |
| <img src="/Assets/Icons/layzspa-heat.svg" width="48px" alt="cust:layzspa-heat"> | cust:layzspa-heat  |
| <img src="/Assets/Icons/layzspa-pump.svg" width="48px" alt="cust:layzspa-pump"> | cust:layzspa-pump  |
| <img src="/Assets/Icons/lg.svg" width="48px" alt="cust:lg"> | cust:lg  |
| <img src="/Assets/Icons/lg-alt.svg" width="48px" alt="cust:lg-alt"> | cust:lg-alt  |
| <img src="/Assets/Icons/lg-thinq.svg" width="48px" alt="cust:lg-thinq"> | cust:lg-thinq  |
| <img src="/Assets/Icons/linkding.svg" width="48px" alt="cust:linkding"> | cust:linkding  |
| <img src="/Assets/Icons/linktap.svg" width="48px" alt="cust:linktap"> | cust:linktap  |
| <img src="/Assets/Icons/logitech.svg" width="48px" alt="cust:logitech"> | cust:logitech  |
| <img src="/Assets/Icons/m&s.svg" width="48px" alt="cust:m&s"> | cust:m&s  |
| <img src="/Assets/Icons/mariadb.svg" width="48px" alt="cust:mariadb"> | cust:mariadb  |
| <img src="/Assets/Icons/mealie.svg" width="48px" alt="cust:mealie"> | cust:mealie  |
| <img src="/Assets/Icons/micro-bit.svg" width="48px" alt="cust:micro-bit"> | cust:micro-bit  |
| <img src="/Assets/Icons/micro-bit-alt.svg" width="48px" alt="cust:micro-bit-alt"> | cust:micro-bit-alt  |
| <img src="/Assets/Icons/micro-bit-alt2.svg" width="48px" alt="cust:micro-bit-alt2"> | cust:micro-bit-alt2  |
| <img src="/Assets/Icons/mqtt-explorer.svg" width="48px" alt="cust:mqtt-explorer"> | cust:mqtt-explorer  |
| <img src="/Assets/Icons/music-assistant.svg" width="48px" alt="cust:music-assistant"> | cust:music-assistant  |
| <img src="/Assets/Icons/network-ups-tools.svg" width="48px" alt="cust:network-ups-tools"> | cust:network-ups-tools  |
| <img src="/Assets/Icons/nhs.svg" width="48px" alt="cust:nhs"> | cust:nhs  |
| <img src="/Assets/Icons/ninja-air-fryer.svg" width="48px" alt="cust:ninja-air-fryer"> | cust:ninja-air-fryer  |
| <img src="/Assets/Icons/node-red.svg" width="48px" alt="cust:node-red"> | cust:node-red  |
| <img src="/Assets/Icons/ntfy.svg" width="48px" alt="cust:ntfy"> | cust:ntfy  |
| <img src="/Assets/Icons/nuaire.svg" width="48px" alt="cust:nuaire"> | cust:nuaire  |
| <img src="/Assets/Icons/octoprint.svg" width="48px" alt="cust:octoprint"> | cust:octoprint  |
| <img src="/Assets/Icons/octoprint-alt.svg" width="48px" alt="cust:octoprint-alt"> | cust:octoprint-alt  |
| <img src="/Assets/Icons/octopus-energy.svg" width="48px" alt="cust:octopus-energy"> | cust:octopus-energy  |
| <img src="/Assets/Icons/ollama.svg" width="48px" alt="cust:ollama"> | cust:ollama  |
| <img src="/Assets/Icons/omada.svg" width="48px" alt="cust:omada"> | cust:omada  |
| <img src="/Assets/Icons/openai.svg" width="48px" alt="cust:openai"> | cust:openai  |
| <img src="/Assets/Icons/paperless.svg" width="48px" alt="cust:paperless"> | cust:paperless  |
| <img src="/Assets/Icons/peanut.svg" width="48px" alt="cust:peanut"> | cust:peanut  |
| <img src="/Assets/Icons/piper.svg" width="48px" alt="cust:piper"> | cust:piper  |
| <img src="/Assets/Icons/planka.svg" width="48px" alt="cust:planka "> | cust:planka  |
| <img src="/Assets/Icons/readarr.svg" width="48px" alt="cust:readarr"> | cust:readarr  |
| <img src="/Assets/Icons/resideo.svg" width="48px" alt="cust:resideo"> | cust:resideo  |
| <img src="/Assets/Icons/resideo-alt.svg" width="48px" alt="cust:resideo-alt"> | cust:resideo-alt  |
| <img src="/Assets/Icons/ring.svg" width="48px" alt="cust:ring"> | cust:ring  |
| <img src="/Assets/Icons/romm.svg" width="48px" alt="cust:romm"> | cust:romm  |
| <img src="/Assets/Icons/sainsburys.svg" width="48px" alt="cust:sainsburys"> | cust:sainsburys  |
| <img src="/Assets/Icons/screwfix.svg" width="48px" alt="cust:screwfix"> | cust:screwfix  |
| <img src="/Assets/Icons/sonoff.svg" width="48px" alt="cust:sonoff"> | cust:sonoff  |
| <img src="/Assets/Icons/sonos.svg" width="48px" alt="cust:sonos"> | cust:sonos  |
| <img src="/Assets/Icons/synology.svg" width="48px" alt="cust:synology"> | cust:synology  |
| <img src="/Assets/Icons/synology-dsm.svg" width="48px" alt="cust:synology-dsm">  | cust:synology-dsm  |
| <img src="/Assets/Icons/tado.svg" width="48px" alt="cust:tado "> | cust:tado  |
| <img src="/Assets/Icons/tasmota.svg" width="48px" alt="cust:tasmota"> | cust:tasmota  |
| <img src="/Assets/Icons/tesco.svg" width="48px" alt="cust:tesco"> | cust:tesco  |
| <img src="/Assets/Icons/toolstation.svg" width="48px" alt="cust:toolstation"> | cust:toolstation  |
| <img src="/Assets/Icons/tp-link.svg" width="48px" alt="cust:tp-link"> | cust:tp-link  |
| <img src="/Assets/Icons/tree-christmas.svg" width="48px" alt="cust:tree-christmas"> | cust:tree-christmas  |
| <img src="/Assets/Icons/vaultwarden.svg" width="48px" alt="cust:vaultwarden"> | cust:vaultwarden  |
| <img src="/Assets/Icons/vscode.svg" width="48px" alt="cust:vscode "> | cust:vscode  |
| <img src="/Assets/Icons/waitrose.svg" width="48px" alt="cust:waitrose"> | cust:waitrose  |
| <img src="/Assets/Icons/watchtower.svg" width="48px" alt="cust:watchtower"> | cust:watchtower  |
| <img src="/Assets/Icons/wemo.svg" width="48px" alt="cust:wemo"> | cust:wemo  |
| <img src="/Assets/Icons/zigbee2mqtt.svg" width="48px" alt="cust:zigbee2mqtt"> | cust:zigbee2mqtt  |
