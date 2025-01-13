{ pkgs }: {
	deps = [
   pkgs.tk
   pkgs.tcl
   pkgs.qhull
   pkgs.pkg-config
   pkgs.gtk3
   pkgs.gobject-introspection
   pkgs.ghostscript
   pkgs.freetype
   pkgs.ffmpeg-full
   pkgs.cairo
		pkgs.python38Full
	];
  env = {
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
  };
}