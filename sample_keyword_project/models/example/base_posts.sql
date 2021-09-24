with posts as (
  select * from {{ ref("posts") }}
),

sentences as (
    select 
        *,
        replace(selftext,'"', '') as self_text,
        split(regexp_replace(self_text, '[!.?]', 'xxx'), 'xxx') as sentence_text_list
    from posts
),

flatten as (
    select 
        *,
        s.value :: text as sentence_text,
        {{ dbt_utils.surrogate_key(['id', 'sentence_text']) }} as sentence_keyword_id
    from sentences,
        lateral flatten(input => sentence_text_list, outer => true) as s
)

select * from flatten