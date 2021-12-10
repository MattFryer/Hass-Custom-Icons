const HA_CUST_ICONS_MAP = {
  hass:
    'M11.992 1.395a.704.704 0 0 0-.498.21L.162 13.099a.563.563 0 0 0-.162.396a.567.567 0 0 0 .566.566H2.67v8.075c0 .26.21.47.47.47h7.948v-3.683l-3.051-3.055a2.42 2.42 0 0 1-.947.193a2.424 2.424 0 0 1-2.422-2.425a2.422 2.422 0 1 1 4.652.947l1.768 1.768v-5.375a2.426 2.426 0 0 1 .908-4.674a2.424 2.424 0 0 1 2.422 2.426a2.425 2.425 0 0 1-1.514 2.248v5.375l1.766-1.768a2.42 2.42 0 0 1-.192-.947a2.423 2.423 0 1 1 4.846 0a2.424 2.424 0 0 1-2.422 2.425a2.42 2.42 0 0 1-.947-.193l-3.05 3.055v3.683h7.947a.47.47 0 0 0 .47-.47V14.06h2.112a.569.569 0 0 0 .396-.162a.567.567 0 0 0 .008-.8l-2.516-2.573V6.471c0-.26-.21-.473-.47-.473h-1.965c-.26 0-.471.212-.471.473v1.103L12.5 1.604a.706.706 0 0 0-.508-.21zm.004 6.36a.97.97 0 0 0 0 1.94a.968.968 0 0 0 .969-.968a.97.97 0 0 0-.969-.971zM7.09 12.667a.968.968 0 0 0-.969.969a.97.97 0 1 0 1.938 0a.968.968 0 0 0-.97-.969zm9.812 0a.97.97 0 1 0 .97.969a.968.968 0 0 0-.97-.969z',
  
  tasmota:
    'M12 0L0 12l1.371 1.372L12 2.743l10.629 10.629L24 12L12 0zm0 8.463a7.41 7.41 0 0 0-2.64 14.334v-2.133a5.464 5.464 0 0 1 1.671-10.17V24h1.94V10.494a5.464 5.464 0 0 1 1.669 10.171v2.133A7.41 7.41 0 0 0 12 8.463z',
  
  alexa:
    'M12 0C5.37 0 0 5.37 0 12c0 6.09 4.53 11.11 10.4 11.9v-2.4a1.59 1.59 0 0 0-1.08-1.53A8.41 8.41 0 0 1 3.6 11.8a8.37 8.37 0 0 1 8.49-8.2a8.4 8.4 0 0 1 8.31 8.71l-.01.07a8.68 8.68 0 0 1-.03.38c0 .07-.01.14-.02.2c0 .08-.01.16-.02.23l-.02.1c-1.03 6.78-9.85 10.58-9.9 10.61c.52.07 1.06.1 1.6.1c6.63 0 12-5.37 12-12S18.63 0 12 0z',
  
  firetv:
    'M20.196 15.12c.265.337-.294 1.73-.542 2.353c-.077.19.085.266.257.123c1.106-.926 1.39-2.867 1.166-3.149c-.226-.277-2.16-.516-3.341.314c-.183.127-.151.304.05.279c.665-.08 2.147-.257 2.41.08m-.858.981c-2.064 1.523-5.056 2.333-7.632 2.333c-3.611 0-6.862-1.334-9.322-3.555c-.194-.176-.02-.414.21-.28c2.655 1.545 5.939 2.477 9.328 2.477c2.287 0 4.803-.476 7.115-1.458c.348-.147.642.231.3.483m2.034-3.155a.388.388 0 0 1-.201-.04c-.041-.026-.087-.1-.133-.225l-1.734-4.355a1.79 1.79 0 0 0-.046-.117a.266.266 0 0 1-.023-.108c0-.084.049-.128.146-.128h.58c.098 0 .165.014.205.04c.04.026.082.102.127.226l1.344 3.823l1.343-3.823c.046-.124.089-.2.128-.226a.402.402 0 0 1 .205-.04h.54c.1 0 .148.044.148.128a.3.3 0 0 1-.025.108c-.016.04-.032.078-.044.117l-1.727 4.355c-.045.124-.09.199-.132.225a.388.388 0 0 1-.201.04zm-3.644.068c-.929 0-1.392-.463-1.392-1.392V8.739h-.706c-.13 0-.197-.066-.197-.196v-.246a.22.22 0 0 1 .045-.147c.03-.031.086-.055.171-.067l.717-.09l.127-1.215c.013-.13.082-.196.207-.196h.41c.13 0 .196.066.196.196v1.196h1.276c.13 0 .195.065.195.197v.372c0 .13-.064.196-.195.196h-1.276v2.834c0 .243.055.411.162.51c.108.098.293.147.555.147c.124 0 .277-.016.46-.049c.099-.02.164-.03.197-.03c.052 0 .088.014.108.044c.02.03.029.077.029.142v.266a.366.366 0 0 1-.04.19c-.026.043-.078.078-.157.103a3.018 3.018 0 0 1-.892.118m-4.665-2.976c.006-.052.011-.137.011-.255c0-.399-.094-.698-.28-.901c-.186-.204-.46-.306-.818-.306c-.412 0-.732.123-.962.369c-.228.245-.36.61-.392 1.093zm-.942 3.07c-.803 0-1.411-.222-1.824-.667c-.412-.444-.616-1.102-.616-1.972c0-.83.204-1.475.616-1.937c.413-.46.988-.691 1.728-.691c.62 0 1.098.176 1.432.524c.332.351.5.846.5 1.487c0 .21-.017.422-.05.638c-.014.077-.034.13-.064.156c-.029.027-.077.04-.142.04h-3.08c.013.563.154.977.418 1.245c.265.268.674.403 1.23.403c.196 0 .385-.014.564-.04a5.04 5.04 0 0 0 .682-.166l.117-.035a.284.284 0 0 1 .09-.016c.085 0 .125.06.125.177v.276c0 .085-.012.144-.037.18a.441.441 0 0 1-.167.114a3.38 3.38 0 0 1-.701.205a4.236 4.236 0 0 1-.82.079m-5.424-.147c-.13 0-.195-.066-.195-.197v-4.58c0-.13.064-.195.195-.195h.432c.064 0 .116.012.153.039c.036.025.06.076.072.146l.07.55c.176-.19.343-.34.499-.452a1.725 1.725 0 0 1 1.02-.323c.079 0 .158.003.235.01c.112.014.168.072.168.176v.53c0 .117-.058.177-.178.177c-.058 0-.114-.004-.17-.01a1.638 1.638 0 0 0-.18-.01c-.524 0-.973.157-1.346.47v3.472c0 .131-.066.197-.195.197zm-2.249 0c-.13 0-.196-.066-.196-.197v-4.58c0-.13.066-.195.196-.195h.579c.13 0 .195.064.195.195v4.58c0 .131-.065.197-.195.197zm.295-5.856c-.19 0-.339-.054-.447-.16a.581.581 0 0 1-.161-.428c0-.176.054-.318.16-.426c.11-.109.257-.163.448-.163c.189 0 .337.054.446.163c.107.108.16.25.16.426a.581.581 0 0 1-.16.427a.608.608 0 0 1-.446.161m-3.625 5.856c-.132 0-.197-.066-.197-.197v-4.01H.195c-.13 0-.195-.066-.195-.197v-.245c0-.065.014-.114.043-.147c.03-.033.088-.055.173-.07l.705-.087v-.804c0-1.091.523-1.638 1.57-1.638c.248 0 .51.036.784.109c.072.019.122.047.152.088c.029.038.044.107.044.205v.255c0 .124-.048.186-.148.186c-.058 0-.14-.01-.248-.029c-.11-.02-.23-.03-.369-.03c-.3 0-.51.057-.633.172c-.121.115-.181.303-.181.564v.903h1.324c.131 0 .197.064.197.195v.373c0 .13-.066.197-.197.197H1.892v4.01c0 .131-.065.197-.196.197z',
  
  esphome:
    'M7.253 2.755c-.676 0-1.231.555-1.231 1.232v.976h-.083a.722.722 0 0 0-.717.716v11.682H.71v-.57h3.544a.355.355 0 0 0 .354-.354v-1.279a.355.355 0 0 0-.354-.355H.709v-.565h3.544a.355.355 0 0 0 .354-.355v-1.278a.355.355 0 0 0-.354-.355H.709v-.569h3.544a.355.355 0 0 0 .354-.355V10.05a.355.355 0 0 0-.354-.354H.709V6.113a.355.355 0 0 0-.355-.355a.355.355 0 0 0-.354.355v3.937a.355.355 0 0 0 .354.355h3.544v.566H.354a.355.355 0 0 0-.354.355v1.279a.355.355 0 0 0 .354.354h3.544v.57H.354a.355.355 0 0 0-.354.354v1.275a.355.355 0 0 0 .354.355h3.544v.57H.354a.355.355 0 0 0-.354.354v1.278a.355.355 0 0 0 .354.355h4.868v.086c0 .389.323.716.717.716h.083v1.14c0 .677.555 1.233 1.231 1.233c.677 0 1.233-.556 1.233-1.232v-1.14h.477v1.137c0 .676.556 1.232 1.232 1.232c.677 0 1.232-.556 1.232-1.232v-1.138h.481v1.138c0 .676.556 1.232 1.232 1.232c.676 0 1.233-.556 1.233-1.232v-1.138h.48v1.138c0 .676.556 1.232 1.232 1.232c.677 0 1.232-.556 1.232-1.232v-1.138h.481v1.138c0 .676.556 1.232 1.232 1.232c.676 0 1.233-.556 1.233-1.232v-1.138h.477v1.138c0 .676.555 1.232 1.231 1.232c.677 0 1.233-.556 1.233-1.232v-1.138h.079c.39 0 .717-.323.717-.716V5.679a.723.723 0 0 0-.714-.716h-.082v-.979c0-.676-.556-1.231-1.232-1.23h-.001a1.238 1.238 0 0 0-1.231 1.233v.976h-.477v-.98c0-.675-.557-1.23-1.233-1.228h-.001c-.676 0-1.23.556-1.23 1.232v.976h-.482v-.976c0-.677-.555-1.232-1.232-1.232c-.676 0-1.232.555-1.232 1.232v.976h-.48v-.976c0-.677-.557-1.232-1.233-1.232s-1.232.555-1.232 1.232v.976h-.48v-.976c0-.677-.556-1.232-1.233-1.232c-.676 0-1.232.555-1.232 1.232v.976h-.477v-.976c0-.677-.556-1.232-1.233-1.232zm0 .715a.51.51 0 0 1 .517.517v.976H6.737v-.976a.51.51 0 0 1 .516-.517zm2.942 0a.51.51 0 0 1 .517.517v.976H9.679v-.976a.51.51 0 0 1 .516-.517zm2.945 0a.51.51 0 0 1 .516.517v.976h-1.032v-.976a.51.51 0 0 1 .516-.517zm2.945 0a.51.51 0 0 1 .517.517v.976h-1.033v-.976a.51.51 0 0 1 .516-.517zm2.945 0h.001a.507.507 0 0 1 .515.513v.98h-1.032v-.976a.51.51 0 0 1 .516-.517zm2.942.001h.001a.507.507 0 0 1 .515.513v.979h-1.032v-.976a.51.51 0 0 1 .516-.516zM6.018 5.758h17.186v12.319H6.018zm8.63 2.777a.322.322 0 0 0-.234.095l-3.776 3.78a.322.322 0 0 0 .228.55h.62v2.225a.322.322 0 0 0 .323.322h5.67a.322.322 0 0 0 .322-.322V12.96h.621a.322.322 0 0 0 .228-.55l-.856-.859v-1.533a.322.322 0 0 0-.322-.323h-.591a.322.322 0 0 0-.323.323v.3L14.87 8.63a.322.322 0 0 0-.221-.095zm-7.91 10.337H7.77v1.14a.51.51 0 0 1-.517.517a.51.51 0 0 1-.516-.516zm2.94 0h1.034v1.138a.51.51 0 0 1-.517.516a.51.51 0 0 1-.516-.516zm2.946 0h1.032v1.138a.51.51 0 0 1-.516.516a.51.51 0 0 1-.516-.516zm2.945 0h1.033v1.138a.51.51 0 0 1-.517.516a.51.51 0 0 1-.516-.516zm2.945 0h1.032v1.138a.51.51 0 0 1-.516.516a.51.51 0 0 1-.516-.516zm2.941 0h1.033v1.138a.51.51 0 0 1-.517.516a.51.51 0 0 1-.516-.516z',
  
  'node-red':
    'M3 0C1.338 0 0 1.338 0 3v6.107h2.858c1.092 0 1.97.868 1.964 1.96v.021c.812-.095 1.312-.352 1.674-.683c.416-.382.69-.91 1.016-1.499c.325-.59.71-1.244 1.408-1.723c.575-.395 1.355-.644 2.384-.686v-.45c0-1.092.88-1.976 1.972-1.976h7.893c1.091 0 1.974.884 1.974 1.976v1.942c0 1.091-.883 2.029-1.974 2.029h-7.893c-1.092 0-1.972-.938-1.972-2.03v-.453c-.853.037-1.408.236-1.798.504c-.48.33-.774.802-1.086 1.368c-.312.565-.63 1.22-1.222 1.763l-.077.069c3.071.415 4.465 1.555 5.651 2.593c1.39 1.215 2.476 2.275 6.3 2.288v-.46c0-1.092.894-1.946 1.986-1.946H24V3c0-1.662-1.338-3-3-3zm10.276 5.41c-.369 0-.687.268-.687.637v1.942c0 .368.318.636.687.636h7.892a.614.614 0 0 0 .635-.636V6.047a.614.614 0 0 0-.635-.636zM0 10.448v3.267h2.858a.696.696 0 0 0 .678-.69v-1.942c0-.368-.31-.635-.678-.635zm4.821 1.67v.907A1.965 1.965 0 0 1 2.858 15H0v6c0 1.662 1.338 3 3 3h18c1.662 0 3-1.338 3-3v-1.393h-2.942c-1.092 0-1.986-.913-1.986-2.005v-.445c-4.046-.032-5.598-1.333-6.983-2.544c-1.437-1.257-2.751-2.431-7.268-2.496zM21.058 15a.644.644 0 0 0-.647.66v1.942c0 .368.278.612.647.612H24V15z',
  
  sonoff:
    'M97.792 21.033c-1.091 1.144-1.267 1.487-.986 1.928.19.3 1.872 2.177 2.319 2.588.206.189.375.409.375.488 0 .079.3.55.667 1.046.366.497.666.977.666 1.068 0 .091.104.226.231.299.128.073.385.433.572.8.929 1.822 1.364 2.754 1.364 2.925 0 .104.141.369.314.588.173.22.365.737.427 1.149.061.412.212.807.333.877.122.07.313.578.425 1.128.112.55.273 1.085.358 1.19.085.105.228.855.319 1.667s.255 1.738.365 2.059c.273.795.265 7.331-.01 8.276-.111.38-.272 1.245-.358 1.922-.086.677-.272 1.453-.413 1.725-.142.272-.259.719-.26.994-.001.275-.147.738-.324 1.03a4.084 4.084 0 0 0-.44 1.166c-.065.351-.257.816-.427 1.035-.17.218-.309.504-.309.633 0 .203-.344.955-.863 1.886-.076.137-.27.51-.43.828-.16.318-.403.702-.54.854-.138.151-.475.658-.75 1.127-.275.468-.558.853-.629.855-.071.001-.201.19-.288.419-.087.23-.23.417-.318.417s-.204.131-.258.292c-.055.16-.585.809-1.178 1.442-.594.632-1.079 1.288-1.079 1.456 0 .553 2.202 2.81 2.74 2.81.283 0 2.26-1.896 2.26-2.167 0-.085.15-.235.333-.333.183-.098.333-.263.333-.367 0-.104.115-.307.254-.452.547-.57 1.246-1.572 1.246-1.787 0-.125.105-.227.234-.227s.319-.207.423-.459c.104-.252.374-.758.599-1.125.225-.366.529-.929.676-1.25.148-.321.364-.696.482-.833a2.17 2.17 0 0 0 .336-.667c.068-.229.22-.529.338-.666.118-.138.295-.553.393-.922.099-.37.291-.82.427-1 .137-.181.251-.516.255-.745.003-.229.124-.642.269-.917.145-.275.335-.938.422-1.473.087-.536.262-1.136.389-1.333.126-.198.278-.885.336-1.527.059-.642.234-1.504.389-1.917.415-1.101.417-8.681.003-9.916-.153-.459-.327-1.328-.385-1.933-.059-.604-.214-1.306-.345-1.559-.132-.253-.309-.896-.395-1.428-.086-.533-.274-1.197-.417-1.475-.144-.278-.262-.622-.262-.764 0-.143-.15-.539-.333-.881-.184-.342-.334-.78-.334-.974 0-.193-.15-.487-.333-.653-.183-.166-.333-.43-.333-.586 0-.156-.188-.56-.417-.898-.229-.338-.417-.719-.417-.847s-.066-.274-.147-.324c-.081-.05-.3-.416-.487-.813-.186-.397-.607-1.073-.936-1.503-.328-.43-.596-.856-.596-.947a.165.165 0 0 0-.164-.165c-.089 0-.307-.283-.483-.628-.176-.345-.59-.922-.92-1.283-.33-.36-.6-.715-.6-.789 0-.073-.115-.134-.255-.134a.411.411 0 0 1-.352-.252c-.598-1.557-1.647-1.573-3.101-.048m-6.125 6.384c-.114.137-.306.25-.426.25s-.266.15-.324.333c-.059.183-.202.333-.318.333-.117 0-.298.188-.402.417-.104.229-.304.417-.443.417-.14 0-.254.088-.254.195 0 .107-.13.339-.289.515-.275.304-.275.33 0 .531.159.117.289.27.289.341 0 .071.169.296.375.499.568.559 1.511 1.731 1.792 2.227.137.243.343.502.458.575.115.073.208.263.208.421 0 .159.123.463.273.677.431.616 1.227 2.158 1.233 2.391.003.116.151.511.328.878.177.366.324.907.327 1.202.003.295.137.895.297 1.334.421 1.151.416 6.779-.006 7.86-.157.401-.285.949-.285 1.217 0 .269-.143.803-.318 1.187a6.98 6.98 0 0 0-.433 1.313c-.063.338-.213.651-.333.697-.12.046-.267.309-.328.584-.06.274-.221.592-.358.706-.137.114-.359.437-.494.72-.451.945-.709 1.342-1.308 2.013-1.507 1.688-1.761 2.02-1.761 2.305 0 .302 2.448 2.943 2.729 2.944.435.003 3.084-3.15 3.349-3.983.061-.192.203-.349.316-.349.113 0 .298-.256.411-.568.112-.312.315-.61.45-.661.134-.052.245-.228.245-.391.001-.163.138-.522.305-.797.168-.275.361-.725.429-1 .069-.275.222-.613.34-.75.118-.138.266-.586.328-.996.062-.41.227-.871.366-1.024.139-.153.295-.718.348-1.254.053-.537.217-1.201.365-1.476.346-.644.405-8.201.067-8.608-.11-.133-.29-.801-.399-1.484-.109-.683-.293-1.354-.41-1.491-.116-.138-.265-.55-.33-.917s-.217-.854-.336-1.083c-.34-.652-1.022-2.211-1.148-2.625-.063-.207-.185-.375-.271-.375-.086 0-.275-.295-.419-.654-.144-.36-.368-.695-.498-.745a.392.392 0 0 1-.237-.338.503.503 0 0 0-.209-.38c-.114-.073-.467-.508-.784-.967-.504-.729-2.066-2.416-2.238-2.416-.034 0-.155.112-.269.25m-8.44 8.5c-.053.137-.165.25-.25.25-.188 0-1.31 1.102-1.31 1.287 0 .073-.15.226-.334.341-.402.251-.46 1.167-.083 1.311.137.053.25.175.25.271 0 .096.206.443.458.771 1.398 1.819 1.936 3.943 1.497 5.901-.149.66-.316 1.438-.373 1.729-.056.29-.201.565-.321.611-.12.046-.271.293-.335.548-.064.256-.261.566-.438.69s-.321.315-.321.426c0 .11-.15.294-.334.408-.706.441.565 2.872 1.501 2.872.079 0 .191.15.249.334.23.722 1.833-.116 2.154-1.126.065-.206.264-.452.441-.547.177-.095.322-.289.322-.432 0-.143.15-.45.333-.683.184-.233.334-.591.334-.796 0-.204.15-.562.333-.795.183-.233.333-.628.333-.877s.161-1.137.358-1.974c.309-1.314.33-1.633.161-2.354a38.459 38.459 0 0 1-.408-2.137c-.117-.717-.293-1.354-.391-1.416-.098-.062-.234-.376-.302-.697-.15-.702-.878-1.995-1.192-2.115a.389.389 0 0 1-.226-.338c0-.71-1.891-2.024-2.106-1.463m-58.983 2.625c-.044.114-.06 12.246-.037 26.958l.043 26.75 17.361.083c9.549.046 17.395.121 17.436.167.421.47.453 1.282.453 11.48v10.668l-.37.259c-.33.231-2.273.26-17.566.26-15.526 0-17.205.025-17.296.263-.056.145-.101 2.989-.101 6.32 0 3.331.045 6.175.101 6.32.174.453 48.068.397 48.352-.057.379-.607.33-49.516-.05-49.793-.244-.179-3.524-.22-17.44-.22-16.168 0-17.147-.017-17.26-.292-.169-.411-.15-25.65.019-25.819.076-.077 7.871-.159 17.323-.183 15.659-.04 17.21-.068 17.486-.317.434-.394.471-12.788.038-12.955-.568-.218-48.409-.112-48.492.108m62.5 40.499c-.044.115-.06 11.272-.037 24.792l.043 24.584h48.833v-49.5l-24.38-.043c-19.416-.033-24.396.001-24.459.167m59.666 0c-.142.371.002 49.093.145 49.237.195.194 12.134.247 12.445.055.219-.135.255-2.317.294-17.702l.044-17.548.373-.288c.344-.266 1.193-.288 11.087-.291l10.715-.004.494.365.493.364v17.277c0 16.525.013 17.288.305 17.552.451.408 11.86.42 12.267.013.237-.237.258-2.649.22-24.708l-.042-24.446-24.38-.043c-19.416-.033-24.396.001-24.46.167m59.525.055c-.262.683-.108 48.488.158 48.867l.259.37h47.758l.198-.375c.151-.285.187-6.187.153-24.708l-.044-24.333-24.191-.043c-21.95-.038-24.199-.017-24.291.222m59.142-.054c-.044.114-.06 11.271-.036 24.791l.042 24.584 6.287.043 6.286.044.243-.377c.2-.312.251-1.648.296-7.699.05-6.787.076-7.349.358-7.708l.305-.387h17.165c11.514 0 17.272-.056 17.488-.172.31-.166.322-.418.322-6.798v-6.624l-.521-.308c-.502-.297-1.165-.304-17.548-.185-14.264.104-17.056.087-17.211-.103-.315-.385-.395-5.118-.098-5.766l.248-.539 17.488-.044c15.329-.039 17.508-.075 17.65-.294.292-.45.127-12.314-.174-12.504-.412-.259-48.491-.215-48.59.046m59.402.067c-.191.23-.237 4.122-.28 23.542-.051 23.683-.027 25.164.41 25.601.296.296 11.702.375 12.463.085l.428-.162v-7.576c0-6.664.031-7.607.262-7.837a8.16 8.16 0 0 0 .292-.302c.016-.022 7.867-.078 17.446-.125l17.417-.085.04-6.75c.024-4.087-.023-6.849-.119-7-.141-.22-2.266-.25-17.473-.25-14.429 0-17.359-.038-17.589-.229-.236-.196-.276-.62-.276-2.954v-2.725l.492-.254c.431-.223 2.597-.255 17.661-.255 16.804 0 17.172-.007 17.341-.322.226-.422.235-11.659.01-12.25l-.162-.428h-24.067c-22.183 0-24.085.022-24.296.276M122.004 92.667c.362.574.2 21.468-.169 21.665-.367.197-21.221.171-21.419-.027-.15-.15-.103-21.519.048-21.667.379-.374 21.303-.346 21.54.029m118.329.149l.417.116v21.485l-10.481.043c-7.604.031-10.544-.009-10.709-.146-.187-.155-.227-2.026-.227-10.647 0-11.036-.024-10.69.75-10.88.523-.128 19.784-.101 20.25.029',
  
  ring:
    'M24 16.375a3.05 3.05 0 0 1-.246 1.231a3.114 3.114 0 0 1-1.672 1.66a3.068 3.068 0 0 1-1.225.247a3.695 3.695 0 0 1-.71-.073a4.05 4.05 0 0 1-.739-.218a3.184 3.184 0 0 1-.676-.37a2.02 2.02 0 0 1-.507-.515a.46.46 0 0 1-.08-.275a.442.442 0 0 1 .152-.346a.504.504 0 0 1 .346-.138a.553.553 0 0 1 .201.04a.392.392 0 0 1 .186.17a.046.046 0 0 0 .016.032l.064.065a1.806 1.806 0 0 0 .798.507a3.052 3.052 0 0 0 .943.154a2.12 2.12 0 0 0 .846-.17a2.189 2.189 0 0 0 1.16-1.16a2.115 2.115 0 0 0 .176-.841v-1.109a3.132 3.132 0 0 1-.985.637a3.089 3.089 0 0 1-1.193.234a3.046 3.046 0 0 1-1.231-.246a3.137 3.137 0 0 1-1.66-1.66a3.04 3.04 0 0 1-.247-1.232v-2.544a3.058 3.058 0 0 1 .247-1.225a3.154 3.154 0 0 1 .668-1a3.202 3.202 0 0 1 .986-.669a3.15 3.15 0 0 1 2.463 0a3.09 3.09 0 0 1 1.668 1.668a3.066 3.066 0 0 1 .246 1.225v5.92zm-.967-5.92a2.118 2.118 0 0 0-.17-.846a2.189 2.189 0 0 0-1.16-1.16a2.201 2.201 0 0 0-1.692 0a2.191 2.191 0 0 0-1.166 1.16a2.134 2.134 0 0 0-.168.845v2.531a2.133 2.133 0 0 0 .168.853a2.194 2.194 0 0 0 .468.693a2.171 2.171 0 0 0 .694.467a2.201 2.201 0 0 0 1.692 0a2.189 2.189 0 0 0 1.16-1.16a2.117 2.117 0 0 0 .174-.853zm-7.252 5.356a.435.435 0 0 1-.154.363a.511.511 0 0 1-.66 0a.434.434 0 0 1-.153-.363v-5.356a2.118 2.118 0 0 0-.17-.846a2.189 2.189 0 0 0-1.16-1.16a2.201 2.201 0 0 0-1.692 0a2.19 2.19 0 0 0-1.16 1.16a2.127 2.127 0 0 0-.17.846v5.356a.434.434 0 0 1-.152.363a.511.511 0 0 1-.661 0a.434.434 0 0 1-.153-.363v-5.356a3.058 3.058 0 0 1 .246-1.225a3.163 3.163 0 0 1 .67-1a3.202 3.202 0 0 1 .984-.669a3.15 3.15 0 0 1 2.464 0a3.091 3.091 0 0 1 1.667 1.668a3.066 3.066 0 0 1 .247 1.225zm-8.383 0a.435.435 0 0 1-.152.363a.511.511 0 0 1-.662 0a.434.434 0 0 1-.152-.363V7.956a.435.435 0 0 1 .152-.363a.512.512 0 0 1 .662 0a.436.436 0 0 1 .152.363zM4.982 8.44a.463.463 0 0 1-.145.338a.483.483 0 0 1-.355.142a.503.503 0 0 1-.339-.145l-.016-.017a.149.149 0 0 0-.032-.024a.123.123 0 0 1-.033-.025a1.9 1.9 0 0 0-1.24-.43q-.871 0-1.363.595q-.491.596-.492 1.693v5.243a.435.435 0 0 1-.153.363a.525.525 0 0 1-.33.123a.525.525 0 0 1-.33-.123a.434.434 0 0 1-.153-.363v-5.243A4.362 4.362 0 0 1 .18 9.303a3.034 3.034 0 0 1 .53-1.031a2.546 2.546 0 0 1 .878-.706a2.763 2.763 0 0 1 1.231-.257a3.08 3.08 0 0 1 1.065.209a2.573 2.573 0 0 1 .934.58a.48.48 0 0 1 .163.343zm2.76-3.128a.826.826 0 0 1-.826.827a.826.826 0 0 1-.827-.827a.826.826 0 0 1 .827-.826a.826.826 0 0 1 .826.826z',
  
  sonos:
   'M12.988 12.36l-2.813-2.634v4.429h.837V11.7l2.813 2.633V9.905h-.837zM6.464 9.665A2.3 2.3 0 0 0 4.13 12c0 1.257 1.077 2.334 2.334 2.334A2.3 2.3 0 0 0 8.798 12a2.3 2.3 0 0 0-2.334-2.334m0 3.83A1.482 1.482 0 0 1 4.968 12c0-.838.658-1.496 1.496-1.496S7.96 11.162 7.96 12s-.658 1.496-1.496 1.496M2.694 12c-.24-.18-.54-.3-.958-.419c-.838-.24-.838-.479-.838-.598c0-.24.299-.48.718-.48c.36 0 .658.18.778.24l.06.06l.658-.479l-.06-.06s-.538-.598-1.436-.598c-.419 0-.838.12-1.137.359c-.3.24-.479.598-.479.958s.18.718.479.957c.24.18.538.3.957.42c.838.239.838.478.838.598c0 .239-.299.478-.718.478c-.359 0-.658-.18-.778-.239l-.06-.06l-.658.479l.06.06s.538.598 1.436.598c.42 0 .838-.12 1.137-.359c.3-.24.48-.598.48-.957c0-.36-.18-.659-.48-.958m14.843-2.334A2.3 2.3 0 0 0 15.202 12a2.337 2.337 0 0 0 2.334 2.334A2.3 2.3 0 0 0 19.87 12a2.337 2.337 0 0 0-2.334-2.334m0 3.83A1.482 1.482 0 0 1 16.04 12c0-.838.658-1.496 1.496-1.496s1.496.658 1.496 1.496s-.718 1.496-1.496 1.496m3.77-1.556c.24.18.54.3.958.42c.838.239.838.478.838.598c0 .239-.299.478-.718.478c-.36 0-.658-.18-.778-.239h-.06l-.658.479l.06.06s.538.598 1.436.598c.419 0 .838-.12 1.137-.359s.479-.598.479-.958s-.18-.718-.479-.957c-.24-.18-.538-.3-.957-.42c-.838-.239-.838-.478-.838-.598c0-.239.299-.478.718-.478c.359 0 .658.18.778.239l.06.06l.658-.479l-.06-.06s-.538-.598-1.436-.598c-.42 0-.838.12-1.137.359c-.3.24-.48.598-.48.957c-.059.36.12.659.48.898',
  
  tado:
    'M22.486 7.795a1.514 1.514 0 1 0 0 3.029a1.514 1.514 0 0 0 0-3.029zm-8.504.003v2.456c-.457-.344-.945-.563-1.686-.563c-1.814 0-2.833 1.364-2.833 3.267c0 1.792 1.019 3.247 2.833 3.247c1.781 0 2.817-1.46 2.82-3.247v-5.16zM1.89 7.799l-1.124.378V9.69H0v.945h.757v3.873c0 .84.67 1.51 1.518 1.51h1.128v-.943h-.946a.566.566 0 0 1-.568-.566v-3.874h3.215V9.69H1.89zm20.596.375a1.135 1.135 0 1 1 0 2.27a1.135 1.135 0 0 1 0-2.27zM5.48 9.69v.946h1.906c.354 0 .549.277.549.54v.773l-1.322-.001c-1.134 0-2.267.769-2.267 2.08c0 1.307 1.13 2.087 2.265 2.087c.953 0 1.326-.57 1.326-.57v.47H9.07v-4.864c0-.784-.667-1.461-1.51-1.461zm12.861.002c-1.808 0-2.835 1.369-2.835 3.237c0 1.911 1.027 3.276 2.835 3.276c1.787 0 2.828-1.36 2.828-3.276c0-1.863-1.046-3.237-2.828-3.237zm-6.046.95c1.14 0 1.68 1.185 1.68 2.316c0 1.117-.55 2.305-1.68 2.305c-1.232 0-1.697-1.188-1.697-2.305c0-1.13.56-2.316 1.697-2.316zm6.046.005c1.12 0 1.703 1.18 1.703 2.3c0 1.117-.572 2.313-1.703 2.313c-1.126 0-1.707-1.165-1.707-2.307c0-1.126.57-2.306 1.707-2.306zM6.614 12.9h1.322v1.207c0 .5-.373 1.062-1.323 1.062c-.367 0-1.133-.19-1.133-1.134c0-.842.758-1.135 1.134-1.135z',
  
  wemo:
    'M4.301 0A4.3 4.3 0 0 0 0 4.302v15.396A4.302 4.302 0 0 0 4.301 24h15.396A4.303 4.303 0 0 0 24 19.699V4.301A4.302 4.302 0 0 0 19.697 0zm12.912 4.167c2.088 0 3.789 1.62 3.789 3.613c0 .095-.004.188-.011.28l-.016.175h-6.324l.114.325c.354.994 1.337 1.663 2.448 1.663c.83 0 1.614-.383 2.1-1.024l.108-.146l.99.674l-.12.16c-.711.943-1.862 1.506-3.078 1.506c-2.09 0-3.79-1.62-3.79-3.613c0-1.993 1.7-3.614 3.79-3.614zm-13.937.132h1.21v4.43a1.325 1.325 0 0 0 2.648 0v-4.43H8.34v4.43a1.325 1.325 0 0 0 2.648 0v-4.43h1.21v4.43a2.535 2.535 0 0 1-2.534 2.532c-.648 0-1.289-.26-1.76-.714l-.168-.162l-.168.162a2.56 2.56 0 0 1-1.76.714a2.535 2.535 0 0 1-2.533-2.532zm13.937 1.024c-.987 0-1.882.517-2.336 1.349l-.195.358h5.06l-.195-.358c-.454-.832-1.348-1.349-2.334-1.349zm-.001 7.233c2.09 0 3.79 1.622 3.79 3.614c0 1.993-1.7 3.613-3.79 3.613s-3.79-1.62-3.79-3.613c0-1.992 1.7-3.614 3.79-3.614zm-11.403.133c.648 0 1.29.26 1.762.713l.166.162l.17-.162a2.562 2.562 0 0 1 1.758-.713a2.536 2.536 0 0 1 2.533 2.532v4.43H10.99v-4.43c0-.73-.595-1.325-1.324-1.325c-.731 0-1.325.595-1.325 1.325v4.43H7.134v-4.43c0-.73-.594-1.325-1.325-1.325c-.73 0-1.323.595-1.323 1.325v4.43h-1.21v-4.43a2.536 2.536 0 0 1 2.533-2.532zm11.403 1.038c-1.422 0-2.58 1.096-2.58 2.443s1.158 2.442 2.58 2.442c1.422 0 2.578-1.095 2.578-2.442c0-1.347-1.156-2.443-2.578-2.443z',

  'tp-link':
    'M15.185 0C10.218 0 6.25 3.984 6.25 8.903V10.8h4.99V8.903c0-2.135 1.736-3.863 3.946-3.863c2.187 0 3.708 1.536 3.708 3.815c0 2.257-1.64 3.912-3.827 3.912h-1.878v5.039h1.878c4.874 0 8.819-4.007 8.819-8.952C23.885 3.72 20.2 0 15.185 0zM.115 12.6v4.103c0 .624.523 1.248 1.236 1.248h4.753v4.801c0 .624.523 1.248 1.236 1.248h4.065V12.6z',
  
  bitwarden:
    'M3.75 0A3.75 3.75 0 0 0 0 3.75v16.5A3.75 3.75 0 0 0 3.75 24h16.5A3.75 3.75 0 0 0 24 20.25V3.75A3.75 3.75 0 0 0 20.25 0zm1.36 2.92h13.8c.208 0 .388.076.54.228a.737.737 0 0 1 .227.539v9.2a5.51 5.51 0 0 1-.401 2.042a7.618 7.618 0 0 1-.995 1.797a11.097 11.097 0 0 1-1.413 1.528c-.547.495-1.052.906-1.515 1.234a19.57 19.57 0 0 1-1.45.928c-.503.291-.86.489-1.072.593a12.88 12.88 0 0 1-.51.24a.687.687 0 0 1-.31.071a.688.688 0 0 1-.312-.072a13.784 13.784 0 0 1-.51-.24a20.61 20.61 0 0 1-1.071-.592a19.133 19.133 0 0 1-1.45-.928a16.457 16.457 0 0 1-1.515-1.234a11.11 11.11 0 0 1-1.414-1.528a7.617 7.617 0 0 1-.994-1.797a5.502 5.502 0 0 1-.401-2.042v-9.2c0-.208.076-.387.227-.54a.737.737 0 0 1 .54-.227zm6.9 2.3v13.62c.95-.502 1.801-1.05 2.552-1.64c1.877-1.47 2.815-2.907 2.815-4.313V5.22z',
  
  'tree-christmas':
    'M12 2 L 11.3125 3.6875 L 9.5 4 L 10.8125 5.1875 L 10.5 7 L 12 6 L 13.5 7 L 13.3125 5.1875 L 14.5 4 L 12.8125 3.6875 Z M 12 7.09375 L 7 12 L 10.125 12 L 5 17 L 8.09375 17 L 3 22 L 21 22 L 16 17 L 19 17 L 14 12 L 16.90625 12z',

};

// Iconset API (Home Assistant 0.110 and up):
async function getIcon(name) {
  return { path: HA_CUST_ICONS_MAP[name] };
}

window.customIconsets = window.customIconsets || {};
window.customIconsets['cust'] = getIcon;

if (!window.frontendVersion || window.frontendVersion < 20200519.0) {
  // ha-iconset-svg (Up to Home Assistant 0.109):
  const iconset = document.createElement("ha-iconset-svg");
  iconset.name = "cust";
  iconset.size = "24";

  let iconsetHTML = '';
  for (let key in HA_CUST_ICONS_MAP) {
    iconsetHTML += `<g id="${key}"><path d="${HA_CUST_ICONS_MAP[key]}" /></g>`;
  }

  iconset.innerHTML = `<svg><defs>${iconsetHTML}</defs></svg>`;
  document.body.appendChild(iconset);
}
  
