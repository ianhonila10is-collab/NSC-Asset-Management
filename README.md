# NSC Asset Management System

A comprehensive Asset Management System for the National Sports Council (NSC) of the Solomon Islands to manage, track, monitor, and report on all government-owned assets throughout their entire lifecycle.

## Overview

This enterprise-grade web application provides complete asset lifecycle management capabilities including:

- **8 Major Asset Categories** (Buildings, Vehicles, Sports Equipment, ICT, Furniture, Maintenance, Consumables, Medical/Emergency)
- **Vehicle Management Module** with registration, service scheduling, and fuel tracking
- **Building & Facility Management** with maintenance scheduling and inspections
- **Inventory Management** with bulk upload/export capabilities
- **Comprehensive Reporting & Dashboards** for asset analytics
- **Role-Based Access Control** with audit trails
- **Digital Asset Verification & Stocktake Module**

## Technology Stack

- **Backend**: Django 4.x + Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 5 + Responsive Mobile-Friendly Design
- **APIs**: RESTful APIs
- **Version Control**: Git

## Project Structure

```
nsc-asset-management/
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── celery.py
├── apps/
│   ├── assets/
│   ├── vehicles/
│   ├── buildings/
│   ├── inventory/
│   ├── reports/
│   ├── users/
│   └── audit/
├── templates/
├── static/
└── docs/
```

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ianhonila10is-collab/nsc-asset-management.git
cd nsc-asset-management
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.example .env
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

## Features

### Asset Management
- Asset registration and categorization
- Barcode/QR code tracking
- Depreciation tracking
- Maintenance scheduling
- Condition assessments
- Transfer and disposal management

### Vehicle Management
- Registration tracking
- Service scheduling
- Fuel consumption monitoring
- Driver assignment
- Accident records
- Insurance tracking

### Building Management
- Facility condition assessments
- Preventative maintenance scheduling
- Infrastructure inspection records
- Utility management
- Defect reporting

### Inventory Management
- Stock tracking
- Reorder levels
- Batch tracking
- Supplier management
- Excel import/export

### Reporting
- Asset register reports
- Vehicle register reports
- Building register reports
- Maintenance reports
- Depreciation reports
- Disposal reports
- Audit reports

## API Documentation

RESTful APIs available for all major modules. See `/docs/api/` for detailed endpoint documentation.

## Security

- Role-Based Access Control (RBAC)
- Multi-level approval workflows
- Comprehensive audit trails
- User activity logging
- Data backup and recovery
- Electronic signatures

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## Support

For support, contact the NSC IT Department.

## License

Government of Solomon Islands - NSC Asset Management System
