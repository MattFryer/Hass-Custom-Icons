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

## Adding More Icons
If you would like to add more icons, please [raise an issue](https://github.com/MattFryer/Hass-Custom-Icons/issues) in the Github repository. Alternatively, add the icons yourself and [raise a pull request](https://github.com/MattFryer/Hass-Custom-Icons/pulls).
