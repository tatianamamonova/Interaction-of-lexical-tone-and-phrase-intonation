# This is a Praat script made for Tanya Mamonova. It analyses multiple selected sounds (TextGrids should be also uploaded to Praat Obects) and search for all labels in first three tiers and returns:
# * file name
# * tier number
# * interval_label
# * pitch
# * time

# This script is distributed under the GNU General Public License.
# George Moroz 01.05.2018

form Get Pitch listing from a file
  comment Where should the script write a result file
  text directory /home/agricolamz/for_work/HSE/students/2017_b2_Mamonova/
  comment How shoul the script name a result file
  text resultfile pitch-log.csv
  comment Time step
  integer step 0.01
  comment Pitch floor (Hz)
  integer floor 75
  comment Pitch ceiling (Hz)
  integer ceiling 250
endform

n = numberOfSelected("Sound")
for i to n
	sound[i] = selected("Sound", i)
endfor
for i to n
	selectObject: sound[i]
	object_name$ = selected$ ("Sound")
	To Pitch... step floor ceiling
	select TextGrid 'object_name$'
		for j from 1 to 3 # change here if you don't want to use first three tiers
			number_of_intervals = Get number of intervals... j
			for b from 1 to number_of_intervals
				select TextGrid 'object_name$'
				interval_label$ = Get label of interval... j 'b'
				if interval_label$ <> ""
					start = Get starting point... 1 'b'
					end = Get end point... 1 'b'
					i = start
					select Pitch 'object_name$'
					while i <= end
						pitch = Get value at time... 'i' Hertz Linear
						i = i + 0.01
						fileappend "'directory$''resultfile$'" 'object_name$''tab$''j''tab$''interval_label$''tab$''pitch''tab$''i''newline$'
					endwhile
				endif
			endfor
		endfor
#	removeObject: "Pitch 'object_name$'"
#	removeObject: "Sound 'object_name$'"
#	removeObject: "TextGrid 'object_name$'"
endfor
