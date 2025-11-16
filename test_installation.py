"""
Test script to verify Data Whisperer installation and functionality
Run this to ensure everything is working correctly
"""

def test_imports():
    """Test that all required modules can be imported"""
    print("🔍 Testing imports...")
    try:
        import flask
        print("  ✅ Flask imported successfully")
        
        import mapper
        print("  ✅ mapper module imported successfully")
        
        import json
        print("  ✅ json module available")
        
        import re
        print("  ✅ re module available")
        
        from difflib import SequenceMatcher
        print("  ✅ difflib available")
        
        return True
    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False


def test_mapper_functions():
    """Test core mapper functionality"""
    print("\n🧪 Testing mapper functions...")
    try:
        from mapper import normalize_field_name, calculate_similarity, extract_fields, suggest_mappings
        
        # Test normalization
        assert normalize_field_name("customerID") == "customer_id"
        assert normalize_field_name("full-name") == "full_name"
        print("  ✅ Field normalization working")
        
        # Test similarity
        score = calculate_similarity("customer_id", "customerId")
        assert score > 0.8
        print(f"  ✅ Similarity calculation working (score: {score})")
        
        # Test field extraction
        test_json = {"user": {"name": "John", "id": 123}, "email": "test@example.com"}
        fields = extract_fields(test_json)
        assert "user.name" in fields
        assert "email" in fields
        print(f"  ✅ Field extraction working (found {len(fields)} fields)")
        
        # Test mapping suggestions
        source = ["customer_id", "full_name", "email_address"]
        target = ["userId", "name", "email"]
        mappings = suggest_mappings(source, target)
        assert len(mappings) == 3
        print(f"  ✅ Mapping suggestions working (generated {len(mappings)} mappings)")
        
        return True
    except Exception as e:
        print(f"  ❌ Mapper test failed: {e}")
        return False


def test_flask_app():
    """Test that Flask app can be initialized"""
    print("\n🌐 Testing Flask application...")
    try:
        from app import app
        assert app is not None
        print("  ✅ Flask app initialized successfully")
        
        # Test that routes exist
        routes = [rule.rule for rule in app.url_map.iter_rules()]
        assert '/' in routes
        assert '/api/analyze' in routes
        assert '/api/preview' in routes
        assert '/api/export' in routes
        print(f"  ✅ All {len(routes)} API routes registered")
        
        return True
    except Exception as e:
        print(f"  ❌ Flask app test failed: {e}")
        return False


def test_static_files():
    """Test that static files exist"""
    print("\n📁 Testing static files...")
    import os
    
    files_to_check = [
        "templates/index.html",
        "static/style.css",
        "static/app.js",
        "README.md"
    ]
    
    all_exist = True
    for file_path in files_to_check:
        if os.path.exists(file_path):
            print(f"  ✅ {file_path} exists")
        else:
            print(f"  ❌ {file_path} missing")
            all_exist = False
    
    return all_exist


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("🔮 Data Whisperer - Installation Test")
    print("=" * 60)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Mapper Functions", test_mapper_functions()))
    results.append(("Flask App", test_flask_app()))
    results.append(("Static Files", test_static_files()))
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary")
    print("=" * 60)
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name:.<40} {status}")
    
    all_passed = all(result[1] for result in results)
    
    print("=" * 60)
    if all_passed:
        print("🎉 All tests passed! Data Whisperer is ready to use.")
        print("\nTo start the application, run:")
        print("  python app.py")
        print("\nThen open: http://localhost:5000")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        print("\nTry running: pip install -r requirements.txt")
    print("=" * 60)
    
    return all_passed


if __name__ == "__main__":
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)
