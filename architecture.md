# System Architecture

## Architecture Overview

The Hostel Issue Management System follows a simple modular architecture.

```text
Student / Admin
       |
       v
    main.py
       |
       +----------------+
       |                |
       v                v
   user.py          issue.py
                        |
                        v
                   storage.py
                        |
                        v
                  issues.json
