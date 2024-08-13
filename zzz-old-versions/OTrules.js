graph TD
    A[Start] --> B[Fetch Overtime Rules from API]
    B --> C[Store Overtime Rules in Local Storage]
    C --> D[Display Form for User Input]
    D --> E[Get User Inputs: Sport, Level, League, Season Type]
    E --> F[Validate Sport Input]
    F --> G{Is Sport Input Valid?}
    G -- Yes --> H[Fetch Appropriate Rules from Storage]
    G -- No --> I[Prompt User for Correct Input]
    H --> J[Differentiation by Season Type]
    J --> K[Display Overtime Rules in Web App]
    K --> L[Get Timeouts and Challenges Info]
    L --> M[Display Timeouts and Challenges Information]
    M --> N{Start Countdown Clock?}
    N -- Yes --> O[Start Real-time Countdown Clock]
    N -- No --> P[End]
    O --> P[End]
