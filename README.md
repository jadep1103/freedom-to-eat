# Freedom to Eat 🍎

A comprehensive food journaling application that helps users track their eating habits, emotions, and overall relationship with food. This app promotes intuitive eating and provides insights into eating patterns through detailed logging and analysis.

## 🎯 Purpose

Freedom to Eat is designed to help users:
- **Track comprehensive food journaling** with detailed context including location, company, emotions, and satisfaction levels
- **Develop mindful eating habits** by encouraging reflection on hunger, fullness, and eating experiences
- **Understand emotional eating patterns** through emotion tracking and meal context analysis
- **Build a healthier relationship with food** through increased awareness and self-reflection

## 🏗️ Architecture

### Backend (FastAPI + PostgreSQL)
- **FastAPI** RESTful API with automatic OpenAPI documentation
- **PostgreSQL** database with SQLAlchemy ORM
- **JWT Authentication** for secure user sessions
- **Image Upload** functionality for food photos
- **Comprehensive data models** for detailed food entry tracking

### Frontend (React + TypeScript)
- **React 18** with TypeScript for type safety
- **React Router** for navigation
- **Context API** for state management
- **Responsive design** for mobile and desktop usage

## ✅ What's Been Done

### 🔐 Authentication System
- [x] User registration and login with JWT tokens
- [x] Protected routes and middleware
- [x] Password hashing and security
- [x] User context management in frontend

### 📊 Food Entry Management
- [x] **Comprehensive food logging** with fields for:
  - Timestamp and meal type (breakfast, lunch, dinner, snack)
  - Location (home, work, gym, restaurant, outside)
  - Company (family, friends, colleagues, alone)
  - Hunger and fullness levels (1-10 scale)
  - Stress, satisfaction, and energy levels (1-10 scale)
  - Emotions tracking (happy, sad, anxious, excited, etc.)
  - Mindful eating indicator
  - Food details and notes
  - Food image uploads

### 🔧 API Endpoints
- [x] Full CRUD operations for food entries
- [x] User-specific data isolation
- [x] Image upload and retrieval
- [x] Authentication endpoints
- [x] Data validation with Pydantic schemas

### 🗄️ Database
- [x] PostgreSQL setup with proper relationships
- [x] UUID-based primary keys
- [x] Enum fields for standardized data
- [x] User-entry relationships

## 🚧 Currently Working On

### Frontend Development
- [x] Basic authentication flow (login/signup)
- [x] Protected routing structure
- [ ] **Food entry form interface** - Building comprehensive forms for creating and editing food entries
- [ ] **Food journal dashboard** - Displaying and managing existing entries
- [ ] **User interface improvements** - Better styling and user experience
- [ ] **Mobile responsiveness** - Ensuring optimal mobile experience

### Data Visualization
- [ ] **Analytics dashboard** - Charts and insights from food entry data
- [ ] **Pattern recognition** - Identifying trends in eating habits and emotions
- [ ] **Progress tracking** - Visual representation of mindful eating progress

## 🎯 Next Steps & Roadmap

### 🤖 NLP Integration
- [ ] **Sentiment analysis** - Analyze emotional content in notes
- [ ] **Smart suggestions** - AI-powered recommendations based on patterns
- [ ] **etc...** 

### ☁️ AWS Deployment
- [ ] **Containerization** - Docker setup for both frontend and backend
- [ ] **AWS Infrastructure**:
  - Application hosting
  - RDS for PostgreSQL database
  - S3 for image storage
  - CloudFront for CDN
  - Application Load Balancer
- [ ] **&more**

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL
- npm or yarn

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
# Configure database connection in config.py
python app/create_tables.py
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 📝 Database Schema

The app uses a comprehensive data model with:
- **Users** - Authentication and profile information
- **Food Entries** - Detailed meal logging with emotional and contextual data
- **Enums** - Standardized options for locations, emotions, meal types, etc.

---

**Freedom to Eat** - Empowering mindful eating through technology 🌱