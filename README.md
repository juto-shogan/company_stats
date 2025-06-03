# company_stats

This was created to test my knowledge on numpy, pandas, seaborn, matplotlib and so on.


A comprehensive Exploratory Data Analysis (EDA) web application built with Streamlit for analysing company sales data. This interactive dashboard provides various analytical insights and visualisations to understand sales patterns, customer behaviour, and business performance.

## 📊 Features

The application offers 10 different analysis tasks:

- **Trend Analysis**: Monthly sales and profit trends over time
- **Geographic Analysis**: Sales and profits comparison by state
- **Discount Analysis**: Scatter plot showing the relationship between discount and profit
- **Shipping Analysis**: Distribution of different ship modes
- **Customer Analysis**: Top 5 customers by sales, profit, and discount
- **Geographic Mapping**: Sales and profit visualisation by state (placeholder)
- **Loyalty Analysis**: Customer order frequency analysis
- **Product Analysis**: Top 10 selling products
- **Category Analysis**: Predominant subcategories in terms of sales
- **Correlation Analysis**: Correlation matrix between discount, sales, and profit

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd company_stats
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your data**
   - Ensure you have a CSV file located at `data/data.csv`
   - The CSV should contain columns: Order Date, Sales, Profit, State, Ship Mode, Customer Name, Product Name, Sub-Category, Discount

### Running the Application

1. **Start the Streamlit server**
   ```bash
   streamlit run app.py
   ```

2. **Access the application**
   - Open your web browser and navigate to `http://localhost:8501`
   - The application will automatically load your dataset and display the dashboard

## 📁 Project Structure

```
company_stats/
├── app.py              # Main Streamlit application
├── data/
│   └── data.csv        # Dataset file
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🛠️ Usage

1. **Dataset Preview**: The app automatically loads and displays the first few rows of your dataset
2. **Analysis Selection**: Use the sidebar to select from 10 different EDA tasks
3. **Interactive Visualizations**: Each analysis generates interactive Plotly charts
4. **Real-time Updates**: Switch between different analyses seamlessly

## 📋 Data Requirements

Your CSV file should include the following columns:
- `Order Date`: Date of the order
- `Sales`: Sales amount
- `Profit`: Profit amount
- `State`: State/region information
- `Ship Mode`: Shipping method
- `Customer Name`: Customer identifier
- `Product Name`: Product identifier
- `Sub-Category`: Product subcategory
- `Discount`: Discount applied

## 🔧 Key Dependencies

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly Express**: Interactive visualizations
- **NumPy**: Numerical computing

## 📧 Contact

For questions or suggestions, reach out to: somtombonu53@gmail.com

## 🎯 Future Enhancements

- Complete geographic mapping functionality
- Export functionality for charts and data
- Advanced filtering options
- Additional statistical analyses
- Data upload interface for custom datasets

---

*This project was created to demonstrate proficiency in data analysis libraries including NumPy, Pandas, and visualisation tools.*
