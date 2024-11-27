-- This code aims at answering the following question per slot of 30 minutes, between which timestamps were
-- the most changes made? Shift your slots per 15 minutes every time (so 12:00AM –12:30AM, 12:15 – 12:45 AM 12:30AM – 01:00 AM etc.)

WITH intervals AS (
    -- Use the reusable macro to generate time slots
    {{ generate_time_slots(
        start_date='2024-10-31 00:00:00',
        end_date='2024-11-01 00:00:00'
    ) }}
),
recent_changes_with_intervals as (
        -- we do a left join between the cleaned_recent_changes and the intervals in order to have a time interval for each row
        -- Note that one change can be in several intervals because of the 15 min shift
        SELECT *
        FROM
            {{ ref('cleaned_recent_changes') }} as crc
            left join intervals as ts
        on crc.timestamp between ts.slot_start and ts.slot_end

),
count_per_interval as(
    select slot_start, slot_end, count(*), RANK() OVER (ORDER BY COUNT(*) DESC) AS rank -- we compute a rank to be able to keep only the interval having the most changes
    from recent_changes_with_intervals
    group by slot_start, slot_end
)

select *
from count_per_interval
where rank = 1