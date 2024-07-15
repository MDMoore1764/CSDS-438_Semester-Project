import h5py


class H5FileParser:

    def __init__(self, h5_file_path: str):
        self.h5 = self.open_h5_file_read(h5_file_path)

    def open_h5_file_read(self, h5_file_path: str):
        return h5py.File(h5_file_path, mode="r")

    def get_num_songs(self):
        """
        Return the number of songs contained in this self.h5 file, i.e. the number of rows
        for all basic informations like name, artist, ...
        """
        return self.h5["metadata"]["songs"]["nrows"]

    def get_artist_familiarity(self, songidx=0):
        """
        Get artist familiarity from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_familiarity"][
            songidx
        ]

    def get_artist_hotttnesss(self, songidx=0):
        """
        Get artist hotttnesss from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_hotttnesss"][
            songidx
        ]

    def get_artist_id(self, songidx=0):
        """
        Get artist id from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_id"][songidx]

    def get_artist_mbid(self, songidx=0):
        """
        Get artist musibrainz id from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_mbid"][songidx]

    def get_artist_playmeid(self, songidx=0):
        """
        Get artist playme id from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_playmeid"][songidx]

    def get_artist_7digitalid(self, songidx=0):
        """
        Get artist 7digital id from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_7digitalid"][
            songidx
        ]

    def get_artist_latitude(self, songidx=0):
        """
        Get artist latitude from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_latitude"][songidx]

    def get_artist_longitude(self, songidx=0):
        """
        Get artist longitude from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_longitude"][songidx]

    def get_artist_location(self, songidx=0):
        """
        Get artist location from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_location"][songidx]

    def get_artist_name(self, songidx=0):
        """
        Get artist name from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["artist_name"][songidx]

    def get_release(self, songidx=0):
        """
        Get release from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["release"][songidx]

    def get_release_7digitalid(self, songidx=0):
        """
        Get release 7digital id from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["release_7digitalid"][
            songidx
        ]

    def get_song_id(self, songidx=0):
        """
        Get song id from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["song_id"][songidx]

    def get_song_hotttnesss(self, songidx=0):
        """
        Get song hotttnesss from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["song_hotttnesss"][songidx]

    def get_title(self, songidx=0):
        """
        Get title from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["title"][songidx]

    def get_track_7digitalid(self, songidx=0):
        """
        Get track 7digital id from a HDF5 song file, by default the first song in it
        """
        return self.h5["metadata"]["songs"]["cols"]["track_7digitalid"][songidx]

    def get_similar_artists(self, songidx=0):
        """
        Get similar artists array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["metadata"]["songs"]["nrows"] == songidx + 1:
            return self.h5["metadata"]["similar_artists"][
                self.h5["metadata"]["songs"]["cols"]["idx_similar_artists"][
                    songidx
                ] :
            ]
        return self.h5["metadata"]["similar_artists"][
            self.h5["metadata"]["songs"]["cols"]["idx_similar_artists"][
                songidx
            ] : self.h5["metadata"]["songs"]["cols"]["idx_similar_artists"][
                songidx + 1
            ]
        ]

    def get_artist_terms(self, songidx=0):
        """
        Get artist terms array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["metadata"]["songs"]["nrows"] == songidx + 1:
            return self.h5["metadata"]["artist_terms"][
                self.h5["metadata"]["songs"]["cols"]["idx_artist_terms"][
                    songidx
                ] :
            ]
        return self.h5["metadata"]["artist_terms"][
            self.h5["metadata"]["songs"]["cols"]["idx_artist_terms"][
                songidx
            ] : self.h5["metadata"]["songs"]["cols"]["idx_artist_terms"][
                songidx + 1
            ]
        ]

    def get_artist_terms_freq(self, songidx=0):
        """
        Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["metadata"]["songs"]["nrows"] == songidx + 1:
            return self.h5["metadata"]["artist_terms_freq"][
                self.h5["metadata"]["songs"]["cols"]["idx_artist_terms"][
                    songidx
                ] :
            ]
        return self.h5["metadata"]["artist_terms_freq"][
            self.h5["metadata"]["songs"]["cols"]["idx_artist_terms"][
                songidx
            ] : self.h5["metadata"]["songs"]["cols"]["idx_artist_terms"][
                songidx + 1
            ]
        ]

    def get_artist_terms_weight(self, songidx=0):
        """
        Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["metadata"]["songs"]["nrows"] == songidx + 1:
            return self.h5["metadata"]["artist_terms_weight"][
                self.h5["metadata"]["songs"]["cols"]["idx_artist_terms"][
                    songidx
                ] :
            ]
        return self.h5["metadata"]["artist_terms_weight"][
            self.h5["metadata"]["songs"]["cols"]["idx_artist_terms"][
                songidx
            ] : self.h5["metadata"]["songs"]["cols"]["idx_artist_terms"][
                songidx + 1
            ]
        ]

    def get_analysis_sample_rate(self, songidx=0):
        """
        Get analysis sample rate from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["analysis_sample_rate"][
            songidx
        ]

    def get_audio_md5(self, songidx=0):
        """
        Get audio MD5 from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["audio_md5"][songidx]

    def get_danceability(self, songidx=0):
        """
        Get danceability from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["danceability"][songidx]

    def get_duration(self, songidx=0):
        """
        Get duration from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["duration"][songidx]

    def get_end_of_fade_in(self, songidx=0):
        """
        Get end of fade in from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["end_of_fade_in"][songidx]

    def get_energy(self, songidx=0):
        """
        Get energy from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["energy"][songidx]

    def get_key(self, songidx=0):
        """
        Get key from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["key"][songidx]

    def get_key_confidence(self, songidx=0):
        """
        Get key confidence from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["key_confidence"][songidx]

    def get_loudness(self, songidx=0):
        """
        Get loudness from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["loudness"][songidx]

    def get_mode(self, songidx=0):
        """
        Get mode from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["mode"][songidx]

    def get_mode_confidence(self, songidx=0):
        """
        Get mode confidence from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["mode_confidence"][songidx]

    def get_start_of_fade_out(self, songidx=0):
        """
        Get start of fade out from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["start_of_fade_out"][
            songidx
        ]

    def get_tempo(self, songidx=0):
        """
        Get tempo from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["tempo"][songidx]

    def get_time_signature(self, songidx=0):
        """
        Get signature from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["time_signature"][songidx]

    def get_time_signature_confidence(self, songidx=0):
        """
        Get signature confidence from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"][
            "time_signature_confidence"
        ][songidx]

    def get_track_id(self, songidx=0):
        """
        Get track id from a HDF5 song file, by default the first song in it
        """
        return self.h5["analysis"]["songs"]["cols"]["track_id"][songidx]

    def get_segments_start(self, songidx=0):
        """
        Get segments start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["segments_start"][
                self.h5["analysis"]["songs"]["cols"]["idx_segments_start"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["segments_start"][
            self.h5["analysis"]["songs"]["cols"]["idx_segments_start"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_segments_start"][
                songidx + 1
            ]
        ]

    def get_segments_confidence(self, songidx=0):
        """
        Get segments confidence array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["segments_confidence"][
                self.h5["analysis"]["songs"]["cols"]["idx_segments_confidence"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["segments_confidence"][
            self.h5["analysis"]["songs"]["cols"]["idx_segments_confidence"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_segments_confidence"][
                songidx + 1
            ]
        ]

    def get_segments_pitches(self, songidx=0):
        """
        Get segments pitches array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["segments_pitches"][
                self.h5["analysis"]["songs"]["cols"]["idx_segments_pitches"][
                    songidx
                ] :,
                :,
            ]
        return self.h5["analysis"]["segments_pitches"][
            self.h5["analysis"]["songs"]["cols"]["idx_segments_pitches"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_segments_pitches"][
                songidx + 1
            ],
            :,
        ]

    def get_segments_timbre(self, songidx=0):
        """
        Get segments timbre array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["segments_timbre"][
                self.h5["analysis"]["songs"]["cols"]["idx_segments_timbre"][
                    songidx
                ] :,
                :,
            ]
        return self.h5["analysis"]["segments_timbre"][
            self.h5["analysis"]["songs"]["cols"]["idx_segments_timbre"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_segments_timbre"][
                songidx + 1
            ],
            :,
        ]

    def get_segments_loudness_max(self, songidx=0):
        """
        Get segments loudness max array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["segments_loudness_max"][
                self.h5["analysis"]["songs"]["cols"][
                    "idx_segments_loudness_max"
                ][songidx] :
            ]
        return self.h5["analysis"]["segments_loudness_max"][
            self.h5["analysis"]["songs"]["cols"]["idx_segments_loudness_max"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"][
                "idx_segments_loudness_max"
            ][
                songidx + 1
            ]
        ]

    def get_segments_loudness_max_time(self, songidx=0):
        """
        Get segments loudness max time array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["segments_loudness_max_time"][
                self.h5["analysis"]["songs"]["cols"][
                    "idx_segments_loudness_max_time"
                ][songidx] :
            ]
        return self.h5["analysis"]["segments_loudness_max_time"][
            self.h5["analysis"]["songs"]["cols"][
                "idx_segments_loudness_max_time"
            ][songidx] : self.h5["analysis"]["songs"]["cols"][
                "idx_segments_loudness_max_time"
            ][
                songidx + 1
            ]
        ]

    def get_segments_loudness_start(self, songidx=0):
        """
        Get segments loudness start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["segments_loudness_start"][
                self.h5["analysis"]["songs"]["cols"][
                    "idx_segments_loudness_start"
                ][songidx] :
            ]
        return self.h5["analysis"]["segments_loudness_start"][
            self.h5["analysis"]["songs"]["cols"]["idx_segments_loudness_start"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"][
                "idx_segments_loudness_start"
            ][
                songidx + 1
            ]
        ]

    def get_sections_start(self, songidx=0):
        """
        Get sections start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["sections_start"][
                self.h5["analysis"]["songs"]["cols"]["idx_sections_start"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["sections_start"][
            self.h5["analysis"]["songs"]["cols"]["idx_sections_start"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_sections_start"][
                songidx + 1
            ]
        ]

    def get_sections_confidence(self, songidx=0):
        """
        Get sections confidence array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["sections_confidence"][
                self.h5["analysis"]["songs"]["cols"]["idx_sections_confidence"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["sections_confidence"][
            self.h5["analysis"]["songs"]["cols"]["idx_sections_confidence"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_sections_confidence"][
                songidx + 1
            ]
        ]

    def get_beats_start(self, songidx=0):
        """
        Get beats start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["beats_start"][
                self.h5["analysis"]["songs"]["cols"]["idx_beats_start"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["beats_start"][
            self.h5["analysis"]["songs"]["cols"]["idx_beats_start"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_beats_start"][
                songidx + 1
            ]
        ]

    def get_beats_confidence(self, songidx=0):
        """
        Get beats confidence array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["beats_confidence"][
                self.h5["analysis"]["songs"]["cols"]["idx_beats_confidence"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["beats_confidence"][
            self.h5["analysis"]["songs"]["cols"]["idx_beats_confidence"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_beats_confidence"][
                songidx + 1
            ]
        ]

    def get_bars_start(self, songidx=0):
        """
        Get bars start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["bars_start"][
                self.h5["analysis"]["songs"]["cols"]["idx_bars_start"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["bars_start"][
            self.h5["analysis"]["songs"]["cols"]["idx_bars_start"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_bars_start"][
                songidx + 1
            ]
        ]

    def get_bars_confidence(self, songidx=0):
        """
        Get bars start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["bars_confidence"][
                self.h5["analysis"]["songs"]["cols"]["idx_bars_confidence"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["bars_confidence"][
            self.h5["analysis"]["songs"]["cols"]["idx_bars_confidence"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_bars_confidence"][
                songidx + 1
            ]
        ]

    def get_tatums_start(self, songidx=0):
        """
        Get tatums start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["tatums_start"][
                self.h5["analysis"]["songs"]["cols"]["idx_tatums_start"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["tatums_start"][
            self.h5["analysis"]["songs"]["cols"]["idx_tatums_start"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_tatums_start"][
                songidx + 1
            ]
        ]

    def get_tatums_confidence(self, songidx=0):
        """
        Get tatums confidence array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["analysis"]["songs"]["nrows"] == songidx + 1:
            return self.h5["analysis"]["tatums_confidence"][
                self.h5["analysis"]["songs"]["cols"]["idx_tatums_confidence"][
                    songidx
                ] :
            ]
        return self.h5["analysis"]["tatums_confidence"][
            self.h5["analysis"]["songs"]["cols"]["idx_tatums_confidence"][
                songidx
            ] : self.h5["analysis"]["songs"]["cols"]["idx_tatums_confidence"][
                songidx + 1
            ]
        ]

    def get_artist_mbtags(self, songidx=0):
        """
        Get artist musicbrainz tag array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["musicbrainz"]["songs"]["nrows"] == songidx + 1:
            return self.h5["musicbrainz"]["artist_mbtags"][
                self.h5["musicbrainz"]["songs"]["cols"]["idx_artist_mbtags"][
                    songidx
                ] :
            ]
        return self.h5["musicbrainz"]["artist_mbtags"][
            self.h5["metadata"]["songs"]["cols"]["idx_artist_mbtags"][
                songidx
            ] : self.h5["metadata"]["songs"]["cols"]["idx_artist_mbtags"][
                songidx + 1
            ]
        ]

    def get_artist_mbtags_count(self, songidx=0):
        """
        Get artist musicbrainz tag count array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the self['h5'] file.
        To get a regular numpy ndarray, cast the result to: numpy['array']( )
        """
        if self.h5["musicbrainz"]["songs"]["nrows"] == songidx + 1:
            return self.h5["musicbrainz"]["artist_mbtags_count"][
                self.h5["musicbrainz"]["songs"]["cols"]["idx_artist_mbtags"][
                    songidx
                ] :
            ]
        return self.h5["musicbrainz"]["artist_mbtags_count"][
            self.h5["metadata"]["songs"]["cols"]["idx_artist_mbtags"][
                songidx
            ] : self.h5["metadata"]["songs"]["cols"]["idx_artist_mbtags"][
                songidx + 1
            ]
        ]

    def get_year(self, songidx=0):
        """
        Get release year from a HDF5 song file, by default the first song in it
        """
        return self.h5["musicbrainz"]["songs"]["cols"]["year"][songidx]
