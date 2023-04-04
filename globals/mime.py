## \package globals.mime

# MIT licensing
# See: docs/LICENSE.txt


from globals.execute import GetCommandOutput
from libdbr          import paths
from libdbr.logger   import getLogger


__logger = getLogger()

## TODO: Doxygen
def GetFileMimeType(filename):
  __logger.deprecated(__name__, GetFileMimeType.__name__, "libdbr.fileinfo.getMimeType")

  # FIXME: need platform independent method to get mimetypes
  CMD_file = paths.getExecutable("file")
  if not CMD_file:
    return "application/octet-stream"
  return GetCommandOutput(CMD_file, ("--mime-type", "--brief", filename,))
