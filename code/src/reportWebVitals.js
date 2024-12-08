const reportWebVitals = (onPerfEntry) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      // CLS (Cumulative Layout Shift)
      getCLS(onPerfEntry);
      
      // FID (First Input Delay)
      getFID(onPerfEntry);
      
      // FCP (First Contentful Paint)
      getFCP(onPerfEntry);
      
      // LCP (Largest Contentful Paint)
      getLCP(onPerfEntry);
      
      // TTFB (Time to First Byte)
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;
