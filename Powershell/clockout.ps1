# powershell script for clocking out

# read user input for clock in time, lunch start, and lunch end
write "use 24hr format.`npress enter after each input.`n enter:"
$prompts = ("(1/3) clock-in time", "(2/3) lunch start time", "(3/3) lunch end time")
$times = @()
foreach ($prompt in $prompts) {$times += read-host $prompt}

# create variables for clock-in, lunch start, lunch end
$clockin_minute = $times[0] % 100
$clockin_hour = ($times[0] - $clockin_minute) / 100
$start_minute = $times[1] % 100
$start_hour = ($times[1] - $start_minute) / 100
$end_minute = $times[2] % 100
$end_hour = ($times[2] - $end_minute) / 100

# calculate time worked (time difference between lunch start and clock-in time)
$minutes_worked = $start_minute - $clockin_minute
switch ($minutes_worked) {
	{$_ -lt 0} {$minutes_worked = [Math]::Abs($minutes_worked); $hours_worked = $start_hour - $clockin_hour -1; break}
	{$_ -ge 0} {$hours_worked = $start_hour - $clockin_hour}
}

# calculate time left to work (time difference between 8 hours and time worked)
$minutes_left = 60 - $minutes_worked


# calculate clock out time (sum of time left to work and lunch end)

# display clock-out time