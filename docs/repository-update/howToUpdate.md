# TO-DO List of things to check in order to update Minecraft server version

## Get new link to Minecraft server jar file

Modify [dockerfile](../../dockerfile) with new link

## Check Server commands, update bot script if needed

Either execute the jar or get documentation about new commands and check for incompatibilities

## Check server-config diff

Check that server-properties from new server version are the same as the old one.

If not update [generate-serverconf](../../utils/generate-serverconf.sh) script

## Check Java version compatibility

In case jar requires new version, [dockerfile](../../dockerfile) should be updated with a new image.

## Check bot custom parsing

Once the previous steps are checked, would not harm to try the parsing with your current command configuration