# Home Assistand Additional Icons

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Additional icons for use in Home Assistant UI

## Installation
It is advised to install via HACS (Home Assistand Community Store).
1. Ensure HACS is already installed on Home Assistant https://hacs.xyz/docs/installation/prerequisites/
2. In Home Assistant, navigate to **HACS** -> **Frontend**
3. Select the 3 dots icon in the top right and choose **Custom repositories**
4. Add this repository `https://github.com/MattFryer/Hass-Custom-Icons`

### Optional - Sitewide availability
By default the icons can only be used inside Lovelace dashbaords. To use the icons site wide, add the following to the `Frontend` sections of your Home Assistant `configuration.yaml`:

```yaml
frontend:
  extra_module_url:
    - /hacsfiles/hass-custom-icons/hass-custom-icons.js
```
## Adding More Icons
If you would like to add more icons, please rasie an issue in the [Github repository](https://github.com/MattFryer/Hass-Custom-Icons/issues).
