package net.pms.configuration;

class LinuxDefaultPaths implements DefaultPaths {

	@Override
	public String getEac3toPath() {
		return "eac3to";
	}

	@Override
	public String getFfmpegPath() {
		return "ffmpeg";
	}

	@Override
	public String getFlacPath() {
		return "flac";
	}

	@Override
	public String getMencoderPath() {
		return "mencoder";
	}

	@Override
	public String getMplayerPath() {
		return "mplayer";
	}

	@Override
	public String getTsmuxerPath() {
		return "linux/tsMuxeR";
	}

	@Override
	public String getVlcPath() {
		return "vlc";
	}

}