CREATE TABLE IF NOT EXISTS incidents (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    title STRING,

    description STRING,

    state STRING,

    author STRING,

    labels STRING[],

    comments INT,

    created_at TIMESTAMPTZ,

    updated_at TIMESTAMPTZ,

    github_url STRING

);