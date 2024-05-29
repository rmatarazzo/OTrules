graph TD
    A[Start]
    B{Choose Sport}
    C{Choose Level}
    D{Choose Gender}
    E{Choose League}
    F[Load Overtime Rules]
    G[Display Rules]
    H[End]
    A --> B
    B -->|One of the major 4| C
    B -->|Other| E
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    