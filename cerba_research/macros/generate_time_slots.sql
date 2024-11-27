{% macro generate_time_slots(start_date, end_date, shift_interval='15 minutes', slot_duration='30 minutes') %}
WITH time_slots AS (
    -- Generate a sequence of timestamps based on the shift interval
    SELECT
        generate_series(
            '{{ start_date }}'::timestamp,
            '{{ end_date }}'::timestamp,
            INTERVAL '{{ shift_interval }}'
        ) AS slot_start
),
intervals AS (
    -- Add the slot duration to create time intervals
    SELECT
        slot_start,
        slot_start + INTERVAL '{{ slot_duration }}' AS slot_end
    FROM
        time_slots
    WHERE
        slot_start < '{{ end_date }}'::timestamp
)
SELECT *
FROM intervals
{% endmacro %}